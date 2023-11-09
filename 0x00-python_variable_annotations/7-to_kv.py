#!/usr/bin/env python3
'''returns a tuple of two parameters'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    '''k is a string and v is either int or float'''
    return tuple((k, v))
