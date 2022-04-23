import unittest
from typing import List
from pprint import pprint

import heapq


class MedianFinder:

    def __init__(self):
        self.small = []  # max heap
        self.big = []  # min heap (python built-tint)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.big, -heapq.heappushpop(self.small, -num))
        if len(self.big) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.big))

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            return (-self.small[0] + self.big[0])/2
        else:
            return -self.small[0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
