#!/usr/bin/env python3
"""function to run multiple coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function call wait_random n times async
    n = num times called
    max_delay = num of delay passed to wait_random
    return list of wait time
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    list = []
    for task in asyncio.as_completed(tasks):
        time: float = await task
        list.append(time)
return list
