import unittest
from typing import List
from pprint import pprint


class Solution:

    def longest_matching_brackets(self, brackets: List[str]) -> int:
        """
        注意这里的dp方向，按矩形的斜线来DP的
        """
        b = brackets
        o2c = {"(": ")", "[": "]"}

        def match(o, c):
            return o in o2c and o2c[o] == c

        N = len(brackets)
        dp = [[0, ]*N for _ in range(N)]
        for l in range(1, N):
            for i in range(N-l):
                j = i+l
                if match(b[i], b[j]):
                    dp[i][j] = max(dp[i][j], 2+dp[i+1][j-1])
                for k in range(i, j):
                    dp[i][j] = max(dp[i][k]+dp[k+1][j], dp[i][j])
        return dp[0][-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        brackets = "((()))"
        expected = 6
        self.assertEqual(sol.longest_matching_brackets(brackets), expected)

    def test_case_2(self):
        sol = Solution()
        brackets = "()()()"
        expected = 6
        self.assertEqual(sol.longest_matching_brackets(brackets), expected)

    def test_case_3(self):
        sol = Solution()
        brackets = "([]])"
        expected = 4
        self.assertEqual(sol.longest_matching_brackets(brackets), expected)

    def test_case_4(self):
        sol = Solution()
        brackets = ")[)("
        expected = 0
        self.assertEqual(sol.longest_matching_brackets(brackets), expected)

    def test_case_5(self):
        sol = Solution()
        brackets = "([][][)"
        expected = 6
        self.assertEqual(sol.longest_matching_brackets(brackets), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
