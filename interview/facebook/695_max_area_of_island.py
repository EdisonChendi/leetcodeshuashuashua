from itertools import count
import unittest
from typing import List
from pprint import pprint

import collections


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        color = 1
        counter = collections.Counter()

        def dfs(i, j):
            grid[i][j] = color
            counter[color] += 1

            for di, dj in DIRs:
                ni, nj = i+di, j+dj
                if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == 1:
                    dfs(ni, nj)

        H, W = len(grid), len(grid[0])
        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 1:
                    color += 1
                    dfs(i, j)

        return max(counter.values(), default=0)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
            0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        expected = 6
        self.assertEqual(sol.maxAreaOfIsland(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
