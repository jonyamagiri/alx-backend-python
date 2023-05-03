#!/usr/bin/env python3
""" module 2-measure_runtime.py """

import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of an asynchronous comprehension.
    Executes the `async_comprehension()` function four times using
     `asyncio.gather()`, and measures the total execution time.
    Returns:
        float: Total execution time of the `async_comprehension()` function.
    Raises:
        None.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed = time.time() - start_time
    return elapsed
