import unittest
from typing import List
from pprint import pprint


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        H, W = len(grid), len(grid[0])

        def start(i, j):
            cnt = 0
            for ni, nj in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] > 0:
                    cnt += 1
            return cnt <= 2

        def dfs(grid, i, j, accu):
            gold, grid[i][j] = grid[i][j], 0
            res = max((dfs(grid, ni, nj, accu+gold)
                      for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
                      if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] > 0), default=accu+gold)
            grid[i][j] = gold
            return res

        return max((dfs(grid, i, j, 0) for i in range(H) for j in range(W) if grid[i][j] > 0 and start(i, j)), default=0)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
        expected = 24
        self.assertEqual(sol.getMaximumGold(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
        expected = 28
        self.assertEqual(sol.getMaximumGold(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
