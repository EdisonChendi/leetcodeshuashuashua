import heapq
import unittest
from typing import List
from pprint import pprint

import math


class Solution1:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # LTE
        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        H, W = len(grid), len(grid[0])
        res = [[-math.inf]*W for _ in range(H)]
        res[0][0] = grid[0][0]

        def dfs(i, j, v):
            for di, dj in DIRs:
                ni, nj = i+di, j+dj
                if 0 <= ni < H and 0 <= nj < W:
                    m = min(grid[ni][nj], v)
                    if m > res[ni][nj]:
                        res[ni][nj] = m
                        dfs(ni, nj, m)

        dfs(0, 0, res[0][0])
        return res[-1][-1]


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # N - number of nodes in grid
        # Time: O(NlgN)
        # Space: O(N)
        def neighbors(i, j):
            res = []
            for di, dj in DIRs:
                ni, nj = i+di, j+dj
                if 0 <= ni < H and 0 <= nj < W:
                    res.append((ni, nj))
            return res

        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        H, W = len(grid), len(grid[0])

        visisted = [[False]*W for _ in range(H)]
        visisted[0][0] = True

        ans = grid[0][0]
        h = [(-grid[0][0], 0, 0)]

        while h:
            v, i, j = heapq.heappop(h)
            ans = min(ans, -v)
            if (i, j) == (H-1, W-1):
                return ans
            for ni, nj in neighbors(i, j):
                if not visisted[ni][nj]:
                    visisted[ni][nj] = True
                    heapq.heappush(h, (-grid[ni][nj], ni, nj))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
        expected = 4
        self.assertEqual(sol.maximumMinimumPath(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7],
                [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]]
        expected = 3
        self.assertEqual(sol.maximumMinimumPath(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
