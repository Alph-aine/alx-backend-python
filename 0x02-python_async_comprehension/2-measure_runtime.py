#!/usr/bin/env python3
'''Runs async_comprehension four times  concurrently'''

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the time to run async_comprehension 4 timmes concurrently'''
    start_time: float = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time: float = time.time()

    total_time: float = end_time - start_time
    return total_time
