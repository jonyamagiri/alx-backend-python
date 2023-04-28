#!/usr/bin/env python3
""" module 102-type_checking.py """
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in a given list by duplicating each item of the list a specified
     number of times.
    Args:
        lst (Tuple): The list of items to be zoomed in.
        factor (int): The number of times each item of the list should be
         duplicated. Default is 2.
    Returns:
        A new list with each item of the original list duplicated `factor`
         number of times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
