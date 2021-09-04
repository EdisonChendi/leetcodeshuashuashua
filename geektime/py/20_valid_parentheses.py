from os import statvfs
import unittest
from typing import List
from pprint import pprint


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        o = set("({[")
        c = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in o:
                stack.append(ch)
            else:
                if not (stack and stack.pop() == c[ch]):
                    return False
        return len(stack) == 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "()"
        expected = True
        self.assertEqual(sol.isValid(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "()[]{}"
        expected = True
        self.assertEqual(sol.isValid(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "(]"
        expected = False
        self.assertEqual(sol.isValid(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "([)]"
        expected = False
        self.assertEqual(sol.isValid(s), expected)

    def test_case_5(self):
        sol = Solution()
        s = "{[]}"
        expected = True
        self.assertEqual(sol.isValid(s), expected)

    def test_case_6(self):
        sol = Solution()
        s = "{[}"
        expected = False
        self.assertEqual(sol.isValid(s), expected)
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
