#!/usr/bin/env python3
"""finding the sum of a list"""
from typing import List


def sum_list(input_list: List(float)) -> float:
    """add all floats in list"""
    sum = 0
    for num in input_list:
        sum += num

    return sum
