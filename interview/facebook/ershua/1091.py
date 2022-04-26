import unittest
from typing import List
from pprint import pprint


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)

        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        DIRs = ((1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1))

        # BFS
        target = (N-1, N-1)
        origin = (0, 0)
        q = [origin]
        visited = {origin}
        res = N*N
        step = 0
        while q:
            step += 1
            nxt_q = []
            while q:
                i, j = q.pop()
                if (i, j) == target:
                    res = min(res, step)
                for di, dj in DIRs:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited and grid[ni][nj] == 0:
                        visited.add((ni, nj))
                        nxt_q.append((ni, nj))
            q = nxt_q

        return res if res < N*N else -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
