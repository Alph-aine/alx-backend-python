#!/usr/bin/env python3
''' Async coroutine that waits for a random number between 0 and max_delay'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''max_delay has a default value of 0'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
