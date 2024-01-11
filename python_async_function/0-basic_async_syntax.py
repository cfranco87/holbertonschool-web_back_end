#!/usr/bin/env python3
"""function using random module"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """using async with ramdom module"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
