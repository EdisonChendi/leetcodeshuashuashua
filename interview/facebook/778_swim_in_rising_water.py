import imp
from msvcrt import kbhit
import unittest
from typing import List
from pprint import pprint

import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def dis(i, j):
            return N-i + N-j

        res = 0
        N = len(grid)
        q = [(grid[0][0], dis(0, 0), 0, 0)]
        seen = set()
        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while True:
            ele, _, i, j = heapq.heappop(q)
            res = max(res, ele)
            if i == N-1 and j == N-1:
                return res
            for di, dj in DIRs:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    heapq.heappush(q, (grid[ni][nj], dis(ni, nj), ni, nj))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[0, 2], [1, 3]]
        expected = 3
        self.assertEqual(sol.swimInWater(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
            12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
        expected = 16
        self.assertEqual(sol.swimInWater(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
