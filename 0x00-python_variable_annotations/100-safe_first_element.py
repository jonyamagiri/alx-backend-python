#!/usr/bin/env python3
""" module 100-safe_first_element.py """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of sequence if there is one, otherwise None.
    Args:
        lst: A sequence of elements of unknown type.
    Returns:
        The first element of the sequence, if there is one, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
