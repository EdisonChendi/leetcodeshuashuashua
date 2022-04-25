import unittest
from typing import List
from pprint import pprint


class Solution1:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack)


class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        l = r = 0
        for ch in s:
            if ch == '(':
                r += 1
            if ch == ')':
                if r > 0:
                    r -= 1
                else:
                    l += 1
        return l + r


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        l = 0
        for ch in s:
            balance += (ch == '(')
            if balance < 0:
                l += 1
                balance = 0
        return l + balance


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
