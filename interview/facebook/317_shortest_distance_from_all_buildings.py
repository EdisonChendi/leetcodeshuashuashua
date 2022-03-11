import unittest
from typing import List
from pprint import pprint

import math


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            res = [[math.inf, ] * W for _ in range(H)]
            q = [(r, c), ]
            visited = [[False, ]*W for _ in range(H)]
            step = 0
            while q:
                nxt_q = []
                while q:
                    i, j = q.pop()
                    for di, dj in DIRs:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == 0 and not visited[ni][nj]:
                            visited[ni][nj] = True
                            nxt_q.append((ni, nj))
                            res[ni][nj] = step+1
                step += 1
                q = nxt_q
            return res

        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        H, W = len(grid), len(grid[0])
        distances = []
        for r, row in enumerate(grid):
            for c, n in enumerate(row):
                if n == 1:
                    distances.append(bfs(r, c))

        ans = math.inf
        for r, row in enumerate(grid):
            for c, n in enumerate(row):
                if n == 0:
                    ans = min(ans, sum(dist[r][c] for dist in distances))
        return ans if ans != math.inf else -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
        expected = 7
        self.assertEqual(sol.shortestDistance(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[1, 0]]
        expected = 1
        self.assertEqual(sol.shortestDistance(grid), expected)

    def test_case_3(self):
        sol = Solution()
        grid = [[1]]
        expected = -1
        self.assertEqual(sol.shortestDistance(grid), expected)

    def test_case_4(self):
        sol = Solution()
        grid = [[1, 1], [0, 1]]
        expected = -1
        self.assertEqual(sol.shortestDistance(grid), expected)

    def test_case_5(self):
        sol = Solution()
        grid = [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [
            1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0]]
        expected = 88
        self.assertEqual(sol.shortestDistance(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
