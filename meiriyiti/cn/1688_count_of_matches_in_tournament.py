import unittest
from typing import List
from pprint import pprint


class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            res += n // 2
            n = (n & 1) + n >> 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 7
        expected = 6
        self.assertEqual(sol.numberOfMatches(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 14
        expected = 13
        self.assertEqual(sol.numberOfMatches(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 8
        expected = 7
        self.assertEqual(sol.numberOfMatches(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
