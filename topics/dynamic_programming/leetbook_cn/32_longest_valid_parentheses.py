from ast import expr_context
from cmath import exp
import re
import unittest
from typing import List
from pprint import pprint
from math import inf


class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        # dp[i] - longest valid parenthese ends with pos i
        L = len(s)
        if L < 2:
            return 0

        dp = [0, ]*L
        for i in range(1, L):
            last_two = s[i-1]+s[i]
            if last_two == "()":
                dp[i] = 2 + (dp[i-2] if i >= 2 else 0)
            elif last_two == "))":
                if i >= 3 and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = 2 + dp[i-1] + \
                        (dp[i - dp[i-1] - 2] if i - dp[i-1] - 2 >= 0 else 0)
        return max(dp)


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i-stack[-1])
                else:
                    stack.append(i)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "(()"
        expected = 2
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = ")()())"
        expected = 4
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = ""
        expected = 0
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "(()()("
        expected = 4
        self.assertEqual(sol.longestValidParentheses(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
