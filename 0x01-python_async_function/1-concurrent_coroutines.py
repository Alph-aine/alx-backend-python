#!/usr/bin/env python3
'''
Asynchronous routine that spawns wait_random
n times with the specified max_delay
'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    n:  number of times to spawn
    max_delay: Maximum delay in seconds
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    return delay
