import unittest
from typing import List
from pprint import pprint


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 4
        expected = False
        self.assertEqual(sol.canWinNim(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
