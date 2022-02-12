import unittest
from typing import List
from pprint import pprint


class Solution1:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < H and 0 <= j < W and grid[i][j] == 1:
                grid[i][j] = 0
                for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    dfs(ni, nj)

        def borders():
            for i in [0, H-1]:
                for j in range(W):
                    yield (i, j)

            for i in range(1, H-1):
                for j in [0, W-1]:
                    yield (i, j)

        H, W = len(grid), len(grid[0])
        for i, j in borders():
            dfs(i, j)

        return sum(grid[i][j] == 1 for i in range(H) for j in range(W))


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def borders():
            for i in [0, H-1]:
                for j in range(W):
                    yield (i, j)

            for i in range(1, H-1):
                for j in [0, W-1]:
                    yield (i, j)

        H, W = len(grid), len(grid[0])

        q = []
        for i, j in borders():
            if grid[i][j] == 1:
                grid[i][j] = 0
                q.append((i, j))
        while q:
            nxt_q = []
            while q:
                i, j = q.pop()
                for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == 1:
                        grid[ni][nj] = 0
                        nxt_q.append((ni, nj))
            q = nxt_q

        return sum(grid[i][j] == 1 for i in range(H) for j in range(W))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        expected = 3
        self.assertEqual(sol.numEnclaves(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        expected = 0
        self.assertEqual(sol.numEnclaves(grid), expected)

    def test_edge_case_1(self):
        sol = Solution()
        grid = [[1]]
        expected = 0
        self.assertEqual(sol.numEnclaves(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
