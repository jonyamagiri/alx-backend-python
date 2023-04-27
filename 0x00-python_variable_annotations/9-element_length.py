#!/usr/bin/env python3
""" module 9-element_length.py """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element of lst and its length.
    Args:
        lst: An iterable object containing sequences.
    Returns:
        A list of tuples containing each element of lst and its length.
    """
    return [(i, len(i)) for i in lst]
