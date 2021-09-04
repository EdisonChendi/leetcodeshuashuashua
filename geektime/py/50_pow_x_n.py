import unittest
from typing import List
from pprint import pprint


class Solution:
    def myPow1(self, x: float, n: int) -> float:
        # recursion
        def pow(x, n):
            if n == 0:
                return 1
            half = pow(x, n//2)
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half

        if n < 0:
            return 1 / pow(x, -n)
        return pow(x, n)

    def myPow(self, x: float, n: int) -> float:
        # iteration
        def pow(x, n):
            res = 1.0
            contribution = x
            while n > 0:
                if n % 2 == 1:
                    res *= contribution
                contribution *= contribution
                n //= 2
            return res

        return pow(x, n) if n >= 0 else 1/pow(x, -n)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        x = 2.00000
        n = 10
        expected = 1024.00000
        self.assertEqual(sol.myPow(x, n), expected)

    def test_case_2(self):
        sol = Solution()
        x = 2.10000
        n = 3
        expected = 9.26100
        self.assertEqual(sol.myPow(x, n), expected)

    def test_case_3(self):
        sol = Solution()
        x = 2.00000
        n = -2
        expected = 0.25000
        self.assertEqual(sol.myPow(x, n), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
