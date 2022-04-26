import unittest
from typing import List
from pprint import pprint


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            nonlocal cnt, color
            cnt += 1
            grid[i][j] = color
            for ni, nj in neighbors(i, j):
                if grid[ni][nj] == 1:
                    dfs(ni, nj)

        counter = [0, 0]
        H, W = len(grid), len(grid[0])
        DIRs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        color = 1

        def neighbors(i, j):
            res = []
            for di, dj in DIRs:
                ni, nj = i+di, j+dj
                if 0 <= ni < H and 0 <= nj < W:
                    res.append((ni, nj))
            return res

        res = 0
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 1:
                    color += 1
                    cnt = 0
                    dfs(i, j)
                    counter.append(cnt)
                    res = max(res, cnt)

        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n != 0:
                    continue
                colors = {grid[ni][nj] for ni, nj in neighbors(i, j)}
                island = 1 + sum(counter[c] for c in colors)
                res = max(res, island)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[1, 0], [0, 1]]
        expected = 3
        self.assertEqual(sol.largestIsland(grid), expected)

    def test_case_1(self):
        sol = Solution()
        grid = [[1, 1], [1, 1]]
        expected = 4
        self.assertEqual(sol.largestIsland(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
