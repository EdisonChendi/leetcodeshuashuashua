import math
import heapq
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        q = [(0, 0), ]
        visited = [[False, ]*N for _ in range(N)]
        step = 1
        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1))
        while q:
            nxt_q = []
            while q:
                r, c = q.pop()
                if r == N-1 and c == N-1:
                    return step
                for i, j in DIRs:
                    ni, nj = r+i, c+j
                    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and grid[ni][nj] == 0:
                        visited[ni][nj] = True
                        nxt_q.append((ni, nj))
            step += 1
            q = nxt_q
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def estimate(r, c):
            return max(N-r, N-c)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        q = [(estimate(0, 0)+1, 1, 0, 0)]
        visited = [[math.inf, ]*N for _ in range(N)]
        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1))

        while q:
            _, stp, r, c = heapq.heappop(q)
            if r == N-1 and c == N-1:
                return stp
            for i, j in DIRs:
                ni, nj = r+i, c+j
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 0 and visited[ni][nj] > stp+1:
                    visited[ni][nj] = stp+1
                    heapq.heappush(q, (estimate(ni, nj)+stp+1, stp+1, ni, nj))
        return -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[0, 1], [1, 0]]
        expected = 2
        self.assertEqual(sol.shortestPathBinaryMatrix(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
        expected = 4
        self.assertEqual(sol.shortestPathBinaryMatrix(grid), expected)

    def test_case_3(self):
        sol = Solution()
        grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
        expected = -1
        self.assertEqual(sol.shortestPathBinaryMatrix(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
