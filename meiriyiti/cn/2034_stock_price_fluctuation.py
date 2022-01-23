import unittest
from typing import List
from pprint import pprint
import heapq


class StockPrice:

    def __init__(self):
        self.min_h = []
        self.max_h = []
        self.timestamp_h = []
        self.counter = 0
        self.versions = {}

    def update(self, timestamp: int, price: int) -> None:
        self.counter += 1
        self.versions[timestamp] = self.counter
        heapq.heappush(self.min_h, (price, timestamp, self.counter))
        heapq.heappush(self.max_h, (-price, timestamp, self.counter))
        heapq.heappush(self.timestamp_h, (-timestamp, price, self.counter))

    def current(self) -> int:
        top = self.timestamp_h[0]
        while top[2] != self.versions[-top[0]]:
            heapq.heappop(self.timestamp_h)
            top = self.timestamp_h[0]
        return top[1]

    def maximum(self) -> int:
        m = self.max_h[0]
        while m[2] != self.versions[m[1]]:
            heapq.heappop(self.max_h)
            m = self.max_h[0]
        return -m[0]

    def minimum(self) -> int:
        m = self.min_h[0]
        while m[2] != self.versions[m[1]]:
            heapq.heappop(self.min_h)
            m = self.min_h[0]
        return m[0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        # obj = StockPrice()
        # obj.update(timestamp,price)
        # param_2 = obj.current()
        # param_3 = obj.maximum()
        # param_4 = obj.minimum()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
