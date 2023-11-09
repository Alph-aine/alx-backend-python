#!/usr/bin/env python3
'''uses List and Union to specify types'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''takes a mixed list of int and floats and returns their sum'''
    return sum(mxd_lst)
