#!/usr/bin/env python3
"""finding the sum of a mixed list, int and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of mixed list"""
    sum = 0
    for num in mxd_lst:
        sum += num

    return sum
