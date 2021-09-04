import unittest
from typing import List
from pprint import pprint
import math

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0,]+[math.inf,]*(n-1)
        for r in range(m):
            dp[0] += grid[r][0]
            for c in range(1, n):
                dp[c] = grid[r][c] + min(dp[c], dp[c-1])
        return dp[-1]

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        expected = 7
        self.assertEqual(sol.minPathSum(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[1,2,3],[4,5,6]]
        expected = 12
        self.assertEqual(sol.minPathSum(grid), expected)

    def test_case_3(self):
        sol = Solution()
        grid = [[1,2],[1,1]]
        expected = 3
        self.assertEqual(sol.minPathSum(grid), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
