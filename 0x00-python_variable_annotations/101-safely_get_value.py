#!/usr/bin/env python3
""" 101-safely_get_value.py """
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')
_def = Union[T, None]
res = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: _def = None) -> res:
    """Return the value of a key in a dictionary if it exists, otherwise
     return a default value.
    Args:
        dct: A mapping object.
        key: A key of any type.
        default: A default value of any type.
    Returns:
        The value of the key in the dictionary if it exists, otherwise the
         default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
