"""
Module used for converting data format to json and json to data format.
"""

from typing import Dict, List, Mapping, Sequence
import json

from tinytim.rows import iterrows
from tinytim.utils import row_dicts_to_data


def data_to_json_list(data: Mapping[str, Sequence]) -> List[Dict]:
    """
    Convert data table to list of row dicts.

    Parameters
    ----------
    data : Mapping[str, Sequence]
        data mapping of {column name: column values}

    Returns
    -------
    list[dict]
        list of row dicts

    Example
    -------
    >>> data = {'x': [1, 2, 3], 'y': [6, 7, 8]}
    >>> data_to_json_list(data)
    [{'x': 1, 'y': 6}, {'x': 2, 'y': 7}, {'x': 3, 'y': 8}]
    """
    return [row for _, row in iterrows(data)]


def json_list_to_data(l: List[Dict]) -> Dict[str, list]:
    """
    Convert list of row dicts to data table format.

    Parameters
    ----------
    l : list[dict]
        list of row dicts

    Returns
    -------
    dict[str, list]
        data dict of {column name: column values}

    Example
    -------
    >>>json = [{'x': 1, 'y': 6}, {'x': 2, 'y': 7}, {'x': 3, 'y': 8}]
    >>> json_list_to_data(json)
    {'x': [1, 2, 3], 'y': [6, 7, 8]}
    """
    return row_dicts_to_data(l)


def data_to_json(data: Mapping[str, Sequence]) -> str:
    """
    Convert data table to list of row dicts json string.

    Parameters
    ----------
    data : Mapping[str, Sequence]
        data mapping of {column name: column values}

    Returns
    -------
    str
        json string, list of row dicts

    Example
    -------
    >>> data = {'x': [1, 2, 3], 'y': [6, 7, 8]}
    >>> data_to_json(data)
    '[{"x": 1, "y": 6}, {"x": 2, "y": 7}, {"x": 3, "y": 8}]'
    """
    l: List[Dict] = data_to_json_list(data)
    return json.dumps(l)


def json_to_data(j: str) -> Dict[str, list]:
    """
    Convert row dicts json string to data dict table.

    Parameters
    ----------
    j : str
        json string, list of row dicts

    Returns
    -------
    Mapping[str, Sequence]
        data mapping of {column name: column values}

    Example
    -------
    >>> j = '[{"x": 1, "y": 6}, {"x": 2, "y": 7}, {"x": 3, "y": 8}]'
    >>> json_to_data(j)
    {'x': [1, 2, 3], 'y': [6, 7, 8]}
    """
    l = json.loads(j)
    return json_list_to_data(l)