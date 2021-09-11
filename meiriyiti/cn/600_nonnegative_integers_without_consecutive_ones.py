import unittest
from typing import List
from pprint import pprint


class Solution:
    def findIntegers(self, n: int) -> int:
        # dp[i][j] i-填0/1，j-是否出现过可以填1的时候填了0
        dp = [[1, 0], [0, 0]]
        bin_rep = bin(n)[2:]
        for i in range(len(bin_rep)):
            ch = bin_rep[i]
            new_dp = [[0, 0], [0, 0]]
            if ch == '1':
                new_dp[0][0] = 0
                new_dp[0][1] = dp[0][0] + dp[1][0] + dp[1][1] + dp[0][1]
                new_dp[1][0] = dp[0][0]
                new_dp[1][1] = dp[0][1]
            else:
                new_dp[0][0] = dp[0][0] + dp[1][0]
                new_dp[0][1] = dp[0][1] + dp[1][1]
                new_dp[1][0] = 0
                new_dp[1][1] = dp[0][1]
            dp = new_dp
        return dp[0][0] + dp[0][1] + dp[1][0] + dp[1][1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 2
        expected = 3
        self.assertEqual(sol.findIntegers(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        expected = 2
        self.assertEqual(sol.findIntegers(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 5
        expected = 5
        self.assertEqual(sol.findIntegers(n), expected)

    def test_case_4(self):
        sol = Solution()
        n = 30
        expected = 13
        self.assertEqual(sol.findIntegers(n), expected)

    def test_case_5(self):
        sol = Solution()
        n = 300
        expected = 76
        self.assertEqual(sol.findIntegers(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
