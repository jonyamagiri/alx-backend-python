#!/usr/bin/env python3
""" 4-tasks.py """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates n tasks for wait_random with the specified max_delay
     and returns a list of the resulting delay times.
    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay time in seconds.
    Returns:
        List[float]: A list of the resulting delay times.
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
