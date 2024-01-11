#!/usr/bin/env python3
"""string and int/float to tuple"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """fucntion returns list of tuple in list"""
    return [(i, len(i)) for i in lst]
