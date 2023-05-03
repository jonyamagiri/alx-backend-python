#!/usr/bin/env python3
""" module 0-async_generator.py """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """An asynchronous generator that yields random floats.
    Yields:
        float: A random float between 0 and 10.
    Raises:
        None.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
