import unittest
from typing import List
from pprint import pprint
from heapq import heappop, heappush, heappushpop
from math import inf


class MedianFinder:

    def __init__(self):
        # make sizes equal, or off by one
        self.big = [inf, ]  # big half - small heap
        self.small = [inf, ]  # small half - big heap

    def addNum(self, num: int) -> None:
        heappush(self.small, -heappushpop(self.big, num))
        if len(self.big) < len(self.small):
            heappush(self.big, -heappop(self.small))

    def findMedian(self) -> float:
        if len(self.big) == len(self.small):
            return (self.big[0] - self.small[0])/2
        else:
            return self.big[0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        obj = MedianFinder()
        obj.addNum(1)
        obj.addNum(2)
        self.assertEqual(obj.findMedian(), 1.5)
        obj.addNum(3)
        self.assertEqual(obj.findMedian(), 2)
        obj.addNum(5)
        self.assertEqual(obj.findMedian(), 2.5)
        obj.addNum(1)
        self.assertEqual(obj.findMedian(), 2)


if __name__ == "__main__":
    unittest.main()
