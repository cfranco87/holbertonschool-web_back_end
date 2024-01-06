#!/usr/bin/env python3
"""function for waiting on task"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    -function call wait_random n times async
    -n - the amount of time random will be called
    -max_delay - the delay for wait_random
    -list of waited time
    -using loop for n
    -as_completed to asynchronously iterate over the completed tasks
    in the time_list. It returns the list of awaited results (floats).
    """
    list = []
    for _ in range(n):
        list.append(task_wait_random(max_delay))
    return [await time for time in asyncio.as_completed(list)]
