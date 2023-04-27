#!/usr/bin/env python3
""" module 7-to_kv.py """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing a string and the square of a given
     int/float value.
    Args:
        k: A string value.
        v: An int or float value.
    Returns:
        A tuple containing a string value k and the square of v as a float.
    """
    return k, float(v ** 2)
