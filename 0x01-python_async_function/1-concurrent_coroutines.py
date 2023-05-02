#!/usr/bin/env python3
""" module 1-concurrent_coroutines.py """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns
     the list of delays in ascending order.
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay time in seconds for each call
         to wait_random.
    Returns:
        List[float]: The list of delays in ascending order.
    """
    results = []
    coroutines = []
    for i in range(n):
        coroutines.append(wait_random(max_delay))
    for coroutine in asyncio.as_completed(coroutines):
        result = await coroutine
        results.append(result)

    return sorted(results)
