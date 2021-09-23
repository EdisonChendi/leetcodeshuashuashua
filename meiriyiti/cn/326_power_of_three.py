import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        i = 1
        while True:
            if i**2 < n:
                i *= i
            else:
                return n == i**2 or n == i**2//3


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 27
        expected = True
        self.assertEqual(sol.isPowerOfThree(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 0
        expected = False
        self.assertEqual(sol.isPowerOfThree(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 45
        expected = False
        self.assertEqual(sol.isPowerOfThree(n), expected)

    def test_case_4(self):
        sol = Solution()
        n = 3**27
        expected = True
        self.assertEqual(sol.isPowerOfThree(n), expected)

    def test_case_5(self):
        sol = Solution()
        n = 3**27-1
        expected = False
        self.assertEqual(sol.isPowerOfThree(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
