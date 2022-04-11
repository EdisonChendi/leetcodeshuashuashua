import unittest
from typing import List
from pprint import pprint

import math


class Solution1:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        def c(n, r):
            f = math.factorial
            return f(n)//f(r)//f(n-r)

        res = 1
        for i in range(1, n+1):
            res += 9 * c(9, i-1)
        return res


class Solution2:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        last = 9
        for i in range(2, n+1):
            cur = last * (9-(i-2))
            ans += cur
            last = cur
        return ans


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 1
        for i in range(1, n+1):
            res += 9 * math.perm(9, i-1)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 2
        expected = 91
        self.assertEqual(sol.countNumbersWithUniqueDigits(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 0
        expected = 1
        self.assertEqual(sol.countNumbersWithUniqueDigits(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
