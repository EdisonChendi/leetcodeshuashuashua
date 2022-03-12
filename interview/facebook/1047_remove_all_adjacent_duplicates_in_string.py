import unittest
from typing import List
from pprint import pprint


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "abbaca"
        expected = "ca"
        self.assertEqual(sol.removeDuplicates(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "azxxzy"
        expected = "ay"
        self.assertEqual(sol.removeDuplicates(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "aa"
        expected = ""
        self.assertEqual(sol.removeDuplicates(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
