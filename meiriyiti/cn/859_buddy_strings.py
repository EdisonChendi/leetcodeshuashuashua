import unittest
from typing import List
from pprint import pprint
from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(goal)
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "ab"
        goal = "ba"
        self.assertEqual(sol.buddyStrings(s, goal), True)

    def test_case_2(self):
        sol = Solution()
        s = "ab"
        goal = "ab"
        self.assertEqual(sol.buddyStrings(s, goal), False)

    def test_case_3(self):
        sol = Solution()
        s = "aa"
        goal = "aa"
        self.assertEqual(sol.buddyStrings(s, goal), True)

    def test_case_4(self):
        sol = Solution()
        s = "aaaaaaabc"
        goal = "aaaaaaacb"
        self.assertEqual(sol.buddyStrings(s, goal), True)

    def test_case_5(self):
        sol = Solution()
        s = "abcd"
        goal = "badc"
        self.assertEqual(sol.buddyStrings(s, goal), False)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
