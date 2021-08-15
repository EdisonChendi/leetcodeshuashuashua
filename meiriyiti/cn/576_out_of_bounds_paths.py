import unittest
from typing import List
from pprint import pprint


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0, ] * n for _ in range(m)] for _ in range(maxMove+1)]
        dp[0][startRow][startColumn] = 1
        res = 0
        for i in range(maxMove):
            for r in range(m):
                for c in range(n):
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            dp[i+1][nr][nc] = (dp[i+1][nr][nc] +
                                               dp[i][r][c]) % MOD
                        else:
                            res = (res+dp[i][r][c]) % MOD
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        m = 2
        n = 2
        maxMove = 2
        startRow = 0
        startColumn = 0
        expected = 6
        self.assertEqual(sol.findPaths(
            m, n, maxMove, startRow, startColumn), expected)

    def test_case_2(self):
        sol = Solution()
        m = 1
        n = 3
        maxMove = 3
        startRow = 0
        startColumn = 1
        expected = 12
        self.assertEqual(sol.findPaths(
            m, n, maxMove, startRow, startColumn), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
