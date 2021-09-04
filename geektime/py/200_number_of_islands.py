import unittest
from typing import List
from pprint import pprint


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find_root(self, i):
        root = i
        while root != self.parent[root]:
            root = self.parent[root]
        while i != self.parent[i]:
            self.parent[i], i = root, self.parent[i]
        return root

    def union(self, i, j):
        root_i = self.find_root(i)
        root_j = self.find_root(j)
        if root_i == root_j:
            return
        self.parent[root_i] = root_j
        self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N, zeros = len(grid), len(grid[0]), 0
        uf = UnionFind(M*N)
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                        if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == "1":
                            uf.union(i*N+j, ni*N+nj)
                else:
                    zeros += 1
        return uf.count - zeros

    def numIslands1(self, grid: List[List[str]]) -> int:
        # by dfs

        def dfs(i, j):
            grid[i][j] = "0"
            for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == "1":
                    dfs(ni, nj)

        M, N, count = len(grid), len(grid[0]), 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        expected = 1
        self.assertEqual(sol.numIslands(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        expected = 3
        self.assertEqual(sol.numIslands(grid), expected)

    def test_case_3(self):
        sol = Solution()
        grid = [
            ["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"]
        ]
        expected = 1
        self.assertEqual(sol.numIslands(grid), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
