#!/usr/bin/env python3
''' Generator function in asyncio'''

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''Generator function yields random numbers between 0 and 10'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
