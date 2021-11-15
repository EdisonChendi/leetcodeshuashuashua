import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 完全平方数，约数的数量为奇数个，灯就是亮着的
        # 那么有多少个完全平方数呢？
        return int(math.sqrt(n+0.5))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        expected = 1
        self.assertEqual(sol.bulbSwitch(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 0
        expected = 0
        self.assertEqual(sol.bulbSwitch(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 1
        expected = 1
        self.assertEqual(sol.bulbSwitch(n), expected)
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
