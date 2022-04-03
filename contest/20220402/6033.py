import unittest
from typing import List
from pprint import pprint


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        ans = 0
        while res > 0:
            res &= (res-1)
            ans += 1
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        start = 10
        goal = 7
        expected = 3
        self.assertEqual(sol.minBitFlips(start, goal), expected)

    def test_case_2(self):
        sol = Solution()
        start = 3
        goal = 4
        expected = 3
        self.assertEqual(sol.minBitFlips(start, goal), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
