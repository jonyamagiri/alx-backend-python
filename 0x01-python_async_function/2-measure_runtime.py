#!/usr/bin/env python3
""" 2-measure_runtime.py """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average runtime of the wait_n coroutine.
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay time in seconds for each
         call to wait_random.
    Returns:
        float: The average elapsed time in seconds per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
