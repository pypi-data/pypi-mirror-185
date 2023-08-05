from __future__ import annotations

import hashlib
import re
from collections import Counter
from collections import defaultdict
from copy import copy
from typing import Callable
from uuid import uuid4

import pyspark.sql.functions as F
from pyspark.sql import Column
from pyspark.sql import DataFrame
from pyspark.sql import Window
from pyspark.sql.types import DataType
from pyspark.sql.types import StructType


class _DeconstructedField:
    def __init__(self, field: str):
        split_field = field.split('.')
        self.levels = copy(split_field)
        self.trunk = split_field.pop(0)
        if len(split_field) > 1:
            *self.branches, self.leaf = split_field
        elif len(split_field) == 0:
            self.branches, self.leaf = [], None
        else:
            self.branches, self.leaf = [], split_field[0]
        self.trunk_and_branches = '.'.join([self.trunk] + self.branches)


def _field_trie(fields: list[str]):
    result = defaultdict(list)
    for field in fields:
        deconstructed_field = _DeconstructedField(field)
        trunk_and_branches = deconstructed_field.trunk_and_branches
        leaf = deconstructed_field.leaf
        result[trunk_and_branches].append(leaf)
    return result


def _fields(
    df: DataFrame,
    include_types: bool,
) -> list[tuple[str, DataType] | str]:
    # ChatGPT 🤖 prompt:
    # write a program that takes a PySpark StructType and returns the leaf node field names, even the nested ones # noqa: E501
    schema = df.schema

    def get_leaf_fields(
        struct: StructType,
        include_types: bool,
    ) -> list[tuple[str, DataType] | str]:
        def _get_leaf_fields(
            struct: StructType,
            prefix: str,
        ) -> list[tuple[str, DataType] | str]:
            fields: list[tuple[str, DataType] | str] = []
            for field in struct:
                if isinstance(field.dataType, StructType):
                    fields.extend(
                        _get_leaf_fields(
                            field.dataType,
                            prefix + field.name + '.',
                        ),
                    )
                else:
                    if include_types:
                        fields.append((prefix + field.name, field.dataType))
                    else:
                        fields.append(prefix + field.name)
            return fields

        return _get_leaf_fields(struct, '')

    return get_leaf_fields(schema, include_types)


def fields(df: DataFrame) -> list[str]:
    """

    Returns names of all of the fields of a DataFrame, including nested ones.

    This contrasts with `StructType.fieldNames` as it gives fully qualified names for nested fields.

    :param df: DataFrame that you want to extract all fields from
    :return: A list of column names, all strings
    """
    return _fields(df, False)


def fields_with_types(df: DataFrame) -> list[tuple[str, DataType]]:
    """

    See docs for `fields`.

    Like `fields`, but returns DataType along with field names as a tuple.

    :param df: DataFrame that you want to extract all fields and types from
    :return: A list of tuples of (column_name, type)
    """
    return _fields(df, True)


def deduplicate_dataframe(
    df: DataFrame,
    keys: list[str] | str = None,
    tiebreaking_columns: list[str] = None,
) -> DataFrame:
    """
    Removes duplicates from a Spark DataFrame.

    :param df: The target Delta Lake table that contains duplicates.
    :param keys: A list of column names used to distinguish rows. The order of this list does not matter.
    :param tiebreaking_columns: A list of column names used for ordering. The order of this list matters, with earlier elements "weighing" more than lesser ones. The columns will be evaluated in descending order. In the event of a tie, you will get non-deterministic results.
    :return: The deduplicated DataFrame
    """
    if keys is None:
        keys = []

    if tiebreaking_columns is None:
        tiebreaking_columns = []

    if isinstance(keys, str):
        keys = [keys]

    if not keys:
        return df.drop_duplicates()

    if df.isStreaming and tiebreaking_columns:
        print('df is streaming, ignoring `tiebreaking_columns`')  # pragma: no cover

    count_col = uuid4().hex  # generate a random column name that is virtually certain to not be in the dataset
    window = Window.partitionBy(keys)

    # noinspection PyTypeChecker
    dupes = df.withColumn(count_col, F.count('*').over(window)).filter(F.col(count_col) > 1).drop(count_col)
    if tiebreaking_columns and not df.isStreaming:
        row_number_col = uuid4().hex
        tiebreaking_desc = [F.col(col).desc() for col in tiebreaking_columns]  # potential enhancement here
        tiebreaking_window = window.orderBy(tiebreaking_desc)
        deduped = (
            dupes.withColumn(row_number_col, F.row_number().over(tiebreaking_window))  # row_number is non-deterministic in the event of ties
            .filter(F.col(row_number_col) == 1)  # take the top row
            .drop(row_number_col)
        )
    else:
        deduped = dupes.drop_duplicates(keys)
    return deduped


def hash_fields(df: DataFrame, denylist_fields: list[str] = None, algorithm: str = 'xxhash64', num_bits=256) -> Column:
    """

    Generates a hash digest of all fields.

    :param df: Input dataframe that is to be hashed.
    :param denylist_fields: Fields that will not be hashed.
    :param algorithm: The function that is used to generate the hash digest, includes:

            * ``xxhash64`` (default) :class:`pyspark.sql.functions.xxhash64`
            * ``md5`` :class:`pyspark.sql.functions.md5`
            * ``sha1`` :class:`pyspark.sql.functions.sha1`
            * ``sha2`` :class:`pyspark.sql.functions.sha2`
            * ``hash`` :class:`pyspark.sql.functions.hash`
    :param num_bits: Only for sha2. The desired bit length of the result.
    :return: A column that represents the hash.
    """
    supported_algorithms = ['sha1', 'sha2', 'md5', 'hash', 'xxhash64']

    if algorithm not in supported_algorithms:
        raise ValueError(f'Algorithm {algorithm} not in supported algorithms {supported_algorithms}')

    all_fields = fields(df)

    if denylist_fields:
        all_fields = list(set(all_fields) - set(denylist_fields))

    all_fields.sort()
    if algorithm == 'sha1':
        hash_col = F.sha1(F.concat_ws('', *all_fields))
    elif algorithm == 'sha2':
        hash_col = F.sha2(F.concat_ws('', *all_fields), num_bits)
    elif algorithm == 'hash':
        hash_col = F.hash(F.concat_ws('', *all_fields))
    elif algorithm == 'xxhash64':
        hash_col = F.xxhash64(F.concat_ws('', *all_fields))
    else:
        hash_col = F.md5(F.concat_ws('', *all_fields))

    return hash_col


def hash_schema(df: DataFrame, denylist_fields: list[str] = None) -> Column:
    """

    Generates a hash digest of a DataFrame's schema. Uses the hashlib.md5 algorithm.

    :param df: Input dataframe whose schema is to be hashed.
    :param denylist_fields: Fields that will not be hashed.
    :return: A column that represents the hash.
    """

    all_fields = fields(df)
    if denylist_fields:
        all_fields = list(set(all_fields) - set(denylist_fields))

    fields_set = set(all_fields)
    if len(all_fields) != len(fields_set):
        dupes = [item for item, count in Counter(all_fields).items() if count > 1]
        raise ValueError(f'Duplicate field(s) detected in df, {dupes}')

    """
    ChatGPT 🤖 prompt:
     python's hash function seems to not be deterministic across sessions. give me a python program that gives the md5 hash of a string (python 3)
    """
    schema_hash = hashlib.md5(''.join(sorted(all_fields)).encode('utf-8')).hexdigest()
    hash_col = F.lit(schema_hash)  # amalgamate list as string bc list is un-hashable
    return hash_col


def _get_fields_by_regex(df: DataFrame, regex: str) -> list[str]:
    # ChatGPT 🤖 prompt:
    # i have a regex pattern string. write a python program that iterates through a list of strings and returns elements that match the regex
    regex = re.compile(regex)
    all_fields = fields(df)
    matches = [field for field in all_fields if regex.search(field)]
    return matches


def _get_fields_by_type(df: DataFrame, target_type: DataType) -> list[str]:
    all_fields = fields_with_types(df)
    print(all_fields)
    pertinent_fields = [field[0] for field in all_fields if field[1] == target_type]
    return pertinent_fields


def _map_fields(df: DataFrame, fields_to_map: list[str], function: Callable) -> DataFrame:
    for field in fields_to_map:
        df = df.withColumn(field, function(field))
    return df


def map_fields_by_regex(df: DataFrame, regex: str, function: Callable) -> DataFrame:
    """

    Apply a function `function` over fields that match a regular expression.

    :param df:
    :param regex: Regular expression pattern. Uses Python's `re` module.
    :param function: Any `pyspark.sql.function` or lambda function that takes a column.
    :return: Resulting DataFrame
    """

    matches = _get_fields_by_regex(df, regex)
    return _map_fields(df, matches, function)


def map_fields_by_type(df: DataFrame, target_type: DataType, function: Callable) -> DataFrame:
    """

    Apply a function `function` over fields that have a target type.

    :param df:
    :param target_type:
    :param function: Any `pyspark.sql.function` or lambda function that takes a column.
    :return: Resulting DataFrame
    """
    pertinent_fields = _get_fields_by_type(df, target_type)
    return _map_fields(df, pertinent_fields, function)


def map_fields(df: DataFrame, field_list: list[str], function: Callable) -> DataFrame:
    """

    Apply a function `function` over fields that are specified in a list.

    :param df:
    :param field_list:
    :param function: Any `pyspark.sql.function` or lambda function that takes a column.
    :return:
    """
    return _map_fields(df, field_list, function)


def select_fields_by_type(df: DataFrame, target_type: DataType):
    """

    :param df:
    :param target_type:
    :return:
    """
    pertinent_fields = _get_fields_by_type(df, target_type)
    return df.select(*pertinent_fields)


def select_fields_by_regex(df: DataFrame, regex: str) -> DataFrame:
    """

    :param df:
    :param regex:
    :return:
    """
    matches = _get_fields_by_regex(df, regex)
    return df.select(*matches)


def _drop_fields(fields_to_drop: tuple[str, list[str | None]]) -> tuple[str, Column]:

    address, leaves = fields_to_drop

    if not leaves or leaves[0] is None:
        raise ValueError(f'Cannot drop top-level field `{address}` with this function. Use df.drop() instead.')

    def _traverse_nest(nest, l, c=0):
        if len(l) == 0:  # termination condition
            return F.col(nest).dropFields(*leaves)
        else:  # recursive step
            current_level = l[0]
            return F.col(nest).withField(current_level, _traverse_nest(f'{nest}.{current_level}', l[1:], c + 1))

    levels = address.split('.')
    if len(levels) == 1:
        return address, F.col(address).dropFields(*leaves)
    col = _traverse_nest(levels[0], levels[1:])
    return levels[0], col


def drop_fields(df: DataFrame, fields_to_drop: list[str]) -> DataFrame:
    """

    Drops a DataFrame's fields, including nested fields and top-level columns.

    :param df:
    :param fields_to_drop: A list of field names that are to be dropped
    :return:
    """
    # potential optimization, use a trie and resolve trie leafs together, as dropFields takes multiple field args

    tries = _field_trie(fields_to_drop)
    for trie in tries.items():
        if trie[1] == [None]:
            df = df.drop(trie[0])
        else:
            name, col = _drop_fields(trie)
            df = df.withColumn(name, col)
    return df


def infer_json_field(df: DataFrame, target_field: str, options: dict[str, str] = None) -> StructType:
    """

    Parses a JSON string and infers its schema.

    :param df:
    :param target_field: A field that contains CSV strings that are to be inferred.
    :param options: Standard csv reader options, including `header`. See :class:pyspark.sql.DataFrameReader.json
    :return: The inferred StructType
    """
    if not options:  # pragma: no cover
        options = dict()
    spark = df.sparkSession
    rdd = df.select(target_field).rdd.map(lambda row: row[0])  # pragma: no cover
    return spark.read.options(**options).json(rdd).schema


def infer_csv_field(df: DataFrame, target_field: str, options: dict[str, str] = None) -> StructType:
    """

    Parses a CSV string and infers its schema.

    :param df:
    :param target_field: A field that contains CSV strings that are to be inferred.
    :param options: Standard csv reader options, including `header`. See :class:pyspark.sql.DataFrameReader.csv
    :return: The inferred StructType
    """
    if not options:  # pragma: no cover
        options = dict()
    spark = df.sparkSession
    rdd = df.select(target_field).rdd.map(lambda row: row[0])  # pragma: no cover
    # noinspection PyTypeChecker
    return spark.read.options(**options).csv(rdd).schema
