import unittest
from typing import List
from pprint import pprint


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # n - 13 - 8+4+1 - 1101
        # 2^1 + 2^4 + 2^8
        def p(x, n):
            a = x
            res = 1
            while n > 0:
                if n & 1 == 1:
                    res *= a
                a *= a
                n >>= 1
            return res

        return p(x, n) if n >= 0 else 1/p(x, -n)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
