import unittest
from typing import List
from pprint import pprint


class Solution1:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif stack:
                stack.pop()
            else:
                ans += 1
        return ans + len(stack)


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0
        for ch in s:
            if ch == '(':
                right += 1
            if ch == ')':
                left += (right == 0)
                right -= (right != 0)
        return left + right


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "())"
        expected = 1
        self.assertEqual(sol.minAddToMakeValid(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "((("
        expected = 3
        self.assertEqual(sol.minAddToMakeValid(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "(())"
        expected = 0
        self.assertEqual(sol.minAddToMakeValid(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "((())"
        expected = 1
        self.assertEqual(sol.minAddToMakeValid(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
