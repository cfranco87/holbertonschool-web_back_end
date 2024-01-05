#!/usr/bin/env python3
"""string and int/float to tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: [Union[int, float]]) -> Tuple[str, float]:
    """ converting a string and int/float to a tuple"""
    kv = (k, v * v)
    return kv
