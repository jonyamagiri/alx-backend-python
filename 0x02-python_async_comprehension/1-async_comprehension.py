#!/usr/bin/env python3
""" module 1-async_comprehension.py """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """An asynchronous comprehension that collects random floats.
    Uses an asynchronous generator to generate random floats and
     collects them in a list.
    Returns:
        List[float]: A list of 10 random floats between 0 and 10.
    Raises:
        None.
    """
    async_generator_result = [i async for i in async_generator()]
    return async_generator_result
