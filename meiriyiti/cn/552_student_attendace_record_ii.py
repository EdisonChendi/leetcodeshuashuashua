import unittest
from typing import List
from pprint import pprint


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9+7
        # dp[n][a][l]
        # dp[n][0][0] dp[n][0][1] dp[n][0][2]
        # dp[n][1][0] dp[n][1][1] dp[n][1][2]
        # dp = [[[0, ]*3 for _ in range(2)] for _ in range(n)]
        dp = [[1, 1, 0], [1, 0, 0]]  # "P" "A" "L"
        for i in range(1, n):
            new_dp = [[0, 0, 0], [0, 0, 0]]
            new_dp[0][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD
            new_dp[0][1] = dp[0][0] % MOD
            new_dp[0][2] = dp[0][1] % MOD
            new_dp[1][0] = (dp[0][0]+dp[0][1]+dp[0][2] +
                            dp[1][0]+dp[1][1]+dp[1][2]) % MOD
            new_dp[1][1] = dp[1][0] % MOD
            new_dp[1][2] = dp[1][1] % MOD
            dp = new_dp
        return sum(sum(a) for a in dp) % MOD


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
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
