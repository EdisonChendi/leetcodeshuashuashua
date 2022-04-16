import unittest
from typing import List
from pprint import pprint


class Solution:
    def largestPalindrome(self, n: int) -> int:
        for m in range(10**(n-1), 10**n)[::-1]:
            if n == 1:
                return 9

            i = m
            while i > 0:
                m = m*10 + i % 10
                i //= 10
            j = 10**n-1
            while j*j >= m:
                if m % j == 0:
                    return m % 1337
                j -= 1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 2
        expected = 987
        self.assertEqual(sol.largestPalindrome(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        expected = 9
        self.assertEqual(sol.largestPalindrome(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
