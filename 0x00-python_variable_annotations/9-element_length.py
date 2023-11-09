#!/usr/bin/env python3
''' Annotation is required for the function below'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''The types here are: Iterable, Sequence, List, Tuple and int'''
    return [(i, len(i)) for i in lst]
