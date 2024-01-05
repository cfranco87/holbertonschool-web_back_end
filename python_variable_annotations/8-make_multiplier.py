#!/usr/bin/env python3
"""string and int/float to tuple"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Using callable we are working with a nested function"""
    def multiplier_function(num: float) -> float:
        return num * multiplier
    return multiplier_function
