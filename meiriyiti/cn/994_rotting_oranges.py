import unittest
from typing import List
from pprint import pprint


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        H, W = len(grid), len(grid[0])
        rotten = set()
        fresh = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 2:
                    rotten.add((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        day = 0
        while rotten:
            nxt_rotten = set()
            while rotten:
                i, j = rotten.pop()
                for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == 1:
                        nxt_rotten.add((ni, nj))
                        grid[ni][nj] = 2
                        fresh -= 1
            rotten = nxt_rotten
            if rotten:
                day += 1
        return day if fresh == 0 else -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        expected = 4
        self.assertEqual(sol.orangesRotting(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        expected = -1
        self.assertEqual(sol.orangesRotting(grid), expected)

    def test_case_3(self):
        sol = Solution()
        grid = [[0, 2]]
        expected = 0
        self.assertEqual(sol.orangesRotting(grid), expected)

    def test_case_4(self):
        sol = Solution()
        grid = [[0]]
        expected = 0
        self.assertEqual(sol.orangesRotting(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
