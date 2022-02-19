import unittest
from typing import List
from pprint import pprint
import functools
import collections


class Solution1:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        DIRS = ((-2, 1), (2, -1), (2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2))

        @functools.cache
        def moves(k, r, c):
            if not (0 <= r < n and 0 <= c < n):
                return 0

            if k == 0:
                return 1

            return sum(moves(k-1, r+i, c+j) for i, j in DIRS)

        return moves(k, row, column) / (8**k)


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = collections.defaultdict(int)
        dp[(row, column)] = 1
        DIRS = ((-2, 1), (2, -1), (2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2))
        for _ in range(k):
            next_dp = collections.defaultdict(int)
            for pos, cnt in dp.items():
                for di, dj in DIRS:
                    ni, nj = pos[0]+di, pos[1]+dj
                    if 0 <= ni < n and 0 <= nj < n:
                        next_dp[(ni, nj)] += cnt
            dp = next_dp
        return sum(dp.values()) / (8**k)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        k = 2
        row = 0
        column = 0
        expected = 0.06250
        self.assertEqual(sol.knightProbability(n, k, row, column), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        k = 0
        row = 0
        column = 0
        expected = 1.000
        self.assertEqual(sol.knightProbability(n, k, row, column), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
