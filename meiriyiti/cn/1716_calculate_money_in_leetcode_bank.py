from cmath import exp
import unittest
from typing import List
from pprint import pprint


class Solution:
    def totalMoney(self, n: int) -> int:
        # 等差数列：
        # Sn = n*a1 + n*(n-1)*d//2
        # s = [1, 3, 6, 10, 15, 21, 28]
        week, day = divmod(n, 7)
        return week*28+week*(week-1)*7//2 + (week+1)*day+day*(day-1)*1//2


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 4
        expected = 10
        self.assertEqual(sol.totalMoney(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 10
        expected = 37
        self.assertEqual(sol.totalMoney(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 20
        expected = 96
        self.assertEqual(sol.totalMoney(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
