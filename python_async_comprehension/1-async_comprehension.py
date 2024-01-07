#!/usr/bin/env python3
"""working with comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehension that gather result from async_generator"""
    return [num async for num in async_generator()]
