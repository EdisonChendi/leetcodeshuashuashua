import unittest
from typing import List
from pprint import pprint


def count_one(n: int) -> int:
    res = 0
    while n > 0:
        res += 1
        n &= n-1
    return res


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(count_one(n) in primes for n in range(left, right+1))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        left = 6
        right = 10
        expected = 4
        self.assertEqual(sol.countPrimeSetBits(left, right), expected)

    def test_case_2(self):
        sol = Solution()
        left = 10
        right = 15
        expected = 5
        self.assertEqual(sol.countPrimeSetBits(left, right), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
