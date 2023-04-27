#!/usr/bin/env python3
""" module 6-sum_mixed_list.py """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a given list of integers and floats.
    Args:
        mxd_lst: A list of integers and/or float numbers.
    Returns:
        The sum of mxd_lst as a float.
    """
    return sum(mxd_lst)
