import unittest
from typing import List
from pprint import pprint

import math


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        N = len(points)
        points.sort(key=lambda p: p[1])
        end = -math.inf
        res = 0
        for i in range(N):
            s, e = points[i]
            if s > end:
                end = e
                res += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        expected = 2
        self.assertEqual(sol.findMinArrowShots(points), expected)

    def test_case_2(self):
        sol = Solution()
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        expected = 4
        self.assertEqual(sol.findMinArrowShots(points), expected)

    def test_case_3(self):
        sol = Solution()
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        expected = 2
        self.assertEqual(sol.findMinArrowShots(points), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
