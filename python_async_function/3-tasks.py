#!/usr/bin/env python3
"""creating function for tasks"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer and returns an asyncio task
    """
    return asyncio.create_task(wait_random(max_delay))
