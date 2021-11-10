from datetime import time
import unittest
from typing import List
from pprint import pprint


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return duration + sum(min(timeSeries[i+1]-timeSeries[i], duration) for i in range(len(timeSeries)-1))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        timeSeries = [1, 4]
        duration = 2
        expected = 4
        self.assertEqual(sol.findPoisonedDuration(
            timeSeries, duration), expected)

    def test_case_2(self):
        sol = Solution()
        timeSeries = [1, 2]
        duration = 2
        expected = 3
        self.assertEqual(sol.findPoisonedDuration(
            timeSeries, duration), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
