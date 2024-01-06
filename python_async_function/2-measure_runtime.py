#!/usr/bin/env python3
"""Measuring total time for n"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    asyncio.run(my_coroutine()) sets up an event loop
    time.perf_counter() It returns the current time in
    seconds with high precision
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
