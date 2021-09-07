import unittest
from typing import List
from pprint import pprint


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res, R, L = 0, 0, 0
        for ch in s:
            R += (ch == 'R')
            L += (ch == 'L')
            if R == L:
                res += 1
                R, L = 0, 0
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "RLRRLLRLRL"
        expected = 4
        self.assertEqual(sol.balancedStringSplit(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "LLLLRRRR"
        expected = 1
        self.assertEqual(sol.balancedStringSplit(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
