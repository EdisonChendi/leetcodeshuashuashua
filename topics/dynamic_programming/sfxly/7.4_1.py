import unittest
from typing import List
from pprint import pprint

"""
题目描述:
给定一个字符串，求把它变成回文的最小代价
可以做的操作: 1.删除某个字符 2.添加某个字符
每个字符的添加/删除操作都有对应的cost
"""


class Solution:

    def min_cost_to_palindrome(self, s, costs):
        """
        dp[i][j], i-start, j-end
        dp[i][j]
            = if s[i] == s[j], dp[i+1][j-1]
            = if s[i] != s[j], min(dp[i+1][j]+w[i], dp[i][j-1]+w[j])
        """
        """
        注意到：这里的递推方向，从下往上，从左往右
        """
        N = len(s)
        dp = [[0]*N for _ in range(N)]
        for i in reversed(range(N)):
            for j in range(i+1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j]+min(costs[s[i]]),
                                   dp[i][j-1]+min(costs[s[j]]))
        return dp[0][-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "abcb"
        costs = {
            "a": (1000, 1100),
            "b": (350, 700),
            "c": (200, 800)
        }
        expected = 900
        self.assertEqual(sol.min_cost_to_palindrome(s, costs), expected)

    def test_case_2(self):
        sol = Solution()
        s = "bacbbb"
        costs = {
            "a": (1000, 1100),
            "b": (350, 700),
            "c": (200, 800)
        }
        expected = 900
        self.assertEqual(sol.min_cost_to_palindrome(s, costs), expected)

    def test_case_3(self):
        sol = Solution()
        s = "bbbb"
        costs = {
            "a": (1000, 1100),
            "b": (350, 700),
            "c": (200, 800)
        }
        expected = 0
        self.assertEqual(sol.min_cost_to_palindrome(s, costs), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
