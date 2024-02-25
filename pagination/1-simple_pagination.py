#!/usr/bin/env python3
"""function that takes two integer arguments"""

import csv
import math
from typing import List


class Server:
    """function that takes two integer arguments"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """function that takes two integer arguments"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """function that takes two integer arguments"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        index_set = index_range(page, page_size)
        first = index_set[0]
        last = index_set[1]
        return self.dataset()[first:last]


def index_range(page, page_size) -> tuple:
    """function that takes two integer arguments"""
    return (page * page_size) - page_size, page * page_size
