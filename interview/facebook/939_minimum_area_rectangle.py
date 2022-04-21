import unittest
from typing import List
from pprint import pprint

import collections

import math


class Solution1:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # group by y
        ys = collections.defaultdict(set)
        for x, y in points:
            ys[y].add(x)
        ys = {y: xs for y, xs in ys.items() if len(xs) > 1}

        res = math.inf
        sorted_y = sorted(ys.keys())
        for i in range(1, len(sorted_y)):
            xs_i = ys[sorted_y[i]]
            for j in range(0, i):
                xs_j = ys[sorted_y[j]]
                xs = sorted(list(xs_i & xs_j))
                if len(xs) > 1:
                    for x1, x2 in zip(xs, xs[1:]):
                        res = min(res, (x2-x1)*(sorted_y[i]-sorted_y[j]))
        return res if res < math.inf else 0


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = math.inf
        points_set = set(tuple(p) for p in points)
        N = len(points)
        for i in range(N):
            xi, yi = points[i]
            for j in range(i+1, N):
                xj, yj = points[j]
                if xi == xj or yi == yj:
                    continue
                if (xi, yj) in points_set and (xj, yi) in points_set:
                    res = min(res, abs((xi-xj)*(yi-yj)))
        return res if res < math.inf else 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
        expected = 4
        self.assertEqual(sol.minAreaRect(points), expected)

    def test_case_2(self):
        sol = Solution()
        points = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
        expected = 2
        self.assertEqual(sol.minAreaRect(points), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
