import unittest
from typing import List
from pprint import pprint


class Solution:
    def checkRecord(self, n: int) -> int:
        M = (10**9) + 7
        # A - 0 1
        # L <= 2 consecutive - 0 1 2
        # P - ok
        # dp[i][j], i - A times, j - L times

        dp = [[1, 0, 0], [0, 0, 0]]
        for _ in range(n):
            new_dp = [[0, 0, 0], [0, 0, 0]]
            new_dp[0][0] = (dp[0][0] + dp[0][2] + dp[0][1]) % M
            new_dp[0][1] = dp[0][0] % M
            new_dp[0][2] = dp[0][1] % M
            new_dp[1][0] = (dp[1][0] + dp[0][0] + dp[0][1] +
                            dp[0][2] + dp[1][2] + dp[1][1]) % M
            new_dp[1][1] = dp[1][0] % M
            new_dp[1][2] = dp[1][1] % M
            dp = new_dp
        return (sum(dp[0]) + sum(dp[1])) % M


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 2
        expected = 8
        self.assertEqual(sol.checkRecord(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        expected = 3
        self.assertEqual(sol.checkRecord(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 10101
        expected = 183236316
        self.assertEqual(sol.checkRecord(n), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
