import unittest
from typing import List
from pprint import pprint


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in 2*goal


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "abcde"
        goal = "cdeab"
        expected = True
        self.assertEqual(sol.rotateString(s, goal), expected)

    def test_case_2(self):
        sol = Solution()
        s = "abcde"
        goal = "abced"
        expected = False
        self.assertEqual(sol.rotateString(s, goal), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
