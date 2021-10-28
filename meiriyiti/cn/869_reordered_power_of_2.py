import unittest
from typing import List
from pprint import pprint


def count_digits(n):
    res = [0]*10
    while n > 0:
        res[n % 10] += 1
        n //= 10
    return tuple(res)


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = {count_digits(1 << i) for i in range(30)}
        return count_digits(n) in nums


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 1
        expected = True
        self.assertEqual(sol.reorderedPowerOf2(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 10
        expected = False
        self.assertEqual(sol.reorderedPowerOf2(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 16
        expected = True
        self.assertEqual(sol.reorderedPowerOf2(n), expected)

    def test_case_4(self):
        sol = Solution()
        n = 24
        expected = False
        self.assertEqual(sol.reorderedPowerOf2(n), expected)

    def test_case_5(self):
        sol = Solution()
        n = 46
        expected = True
        self.assertEqual(sol.reorderedPowerOf2(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
