#!/usr/bin/env python3
"""function that takes list"""
from typing import List


def sum_list(input_list: List[float])-> float:
    """takes list of floats returns float
    @input_list: list of floats to add up
    return sum of list
    """
    result = 0
    for num in input_list:
        result += num

    return result
