#!/usr/bin/env python3
"""working with async generator"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    -generators work with iterables
    -uniform(a, b) function is used
    to generate a random floating-point number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(1, 10)
