#!/usr/bin/env python3
'''Measures the time used for an asycn function'''

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Muultiple coroutines are run concurrently using asyncio.gather'''
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()

    total_time: float = end_time - start_time
    return total_time / n
