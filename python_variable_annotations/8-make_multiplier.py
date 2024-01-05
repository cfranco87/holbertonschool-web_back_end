#!/usr/bin/env python3
"""string and int/float to tuple"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make a multiplier"""
    def multi(value: float) -> float:
        return multiplier * value
    return multi
