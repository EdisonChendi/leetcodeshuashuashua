import unittest
from typing import List
from pprint import pprint


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        cur_color = 0
        color = [[0]*N for _ in range(N)]
        cnt = {}
        accu = 0

        def neighbors(r, c):
            return ((nr, nc) for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] if 0 <= nr < N and 0 <= nc < N)

        def dfs(r, c):
            nonlocal accu
            color[r][c] = cur_color
            accu += 1
            cnt[cur_color] = accu
            for nr, nc in neighbors(r, c):
                if color[nr][nc] == 0 and grid[nr][nc] == 1:
                    dfs(nr, nc)

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1 and color[i][j] == 0:
                    cur_color += 1
                    accu = 0
                    dfs(i, j)

        ans = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    ans = max(ans, cnt[color[i][j]])
                if grid[i][j] == 0:
                    distinct_paths = {color[ni][nj] for ni, nj in neighbors(i, j)
                                      if grid[ni][nj] == 1}
                    ans = max(ans, 1+sum(cnt[p] for p in distinct_paths))
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[1, 0], [0, 1]]
        expected = 3
        self.assertEqual(sol.largestIsland(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[1, 1], [1, 0]]
        expected = 4
        self.assertEqual(sol.largestIsland(grid), expected)

    def test_case_3(self):
        sol = Solution()
        grid = [[1, 1], [1, 1]]
        expected = 4
        self.assertEqual(sol.largestIsland(grid), expected)

    def test_case_4(self):
        sol = Solution()
        grid = [[1, 1, 0], [1, 1, 0], [1, 0, 0]]
        expected = 6
        self.assertEqual(sol.largestIsland(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
