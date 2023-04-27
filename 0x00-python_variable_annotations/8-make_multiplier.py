#!/usr/bin/env python3
""" module 8-make_multiplier.py """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier.
    Args:
        multiplier: A float value to multiply by.
    Returns:
        A function that takes a float argument and returns its product
        with the multiplier.
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
#  return lambda x: x * multiplier
