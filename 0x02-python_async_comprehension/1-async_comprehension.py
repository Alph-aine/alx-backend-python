#!/usr/bin/env python3
'''Async coroutine used ass an iterable'''

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Returns the random numbers generated in async_generator in a list'''
    return [number async for number in async_generator()]
