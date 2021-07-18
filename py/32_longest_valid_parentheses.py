import unittest
from typing import List
from pprint import pprint


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = ")"+s
        N = len(s)
        dp = [0, ]*N

        for i in range(1, N):
            ch = s[i]
            if ch == "(":
                continue
            if s[i-1] == "(":
                dp[i] = 2 + dp[i-2]
            if s[i-1] == ")" and s[i-dp[i-1]-1] == "(":
                dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]-2]

        return max(dp)

    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1, ]
        for i, ch in enumerate(s):
            if ch == "(":
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
        s = ")(()()()())"
        expected = 10
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "()(()"
        expected = 2
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_5(self):
        sol = Solution()
        s = "()(())"
        expected = 6
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_6(self):
        sol = Solution()
        s = "(()(((()"
        expected = 2
        self.assertEqual(sol.longestValidParentheses(s), expected)

    def test_case_7(self):
        sol = Solution()
        s = "()((()))"
        expected = 8
        self.assertEqual(sol.longestValidParentheses(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()
    #     s = ""
    #     expected = 0
    #     self.assertEqual(sol.longestValidParentheses(s), expected)


if __name__ == "__main__":
    unittest.main()
