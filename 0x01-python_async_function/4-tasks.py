#!/usr/bin/env python3
'''running tasks'''

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    n:  number of times to spawn
    max_delay: Maximum delay in seconds
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    return sorted(delay)
