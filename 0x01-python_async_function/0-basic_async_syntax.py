#!/usr/bin/env python3
""" module 0-basic_async_syntax.py """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive).
    Args:
        max_delay (int): The maximum delay time in seconds (default 10).
    Returns:
        float: The amount of time waited.
    """
    random_time = random.random() * max_delay
    await asyncio.sleep(random_time)
    return random_time
