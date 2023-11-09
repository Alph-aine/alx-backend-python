#!/usr/bin/env python3
'''uses List and Union to specify types'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''takes a mixed list of int and floats and returns their sum'''
    return sum(mxd_lst)
