import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = math.inf
        for p in prices:
            lowest = min(p, lowest)
            max_profit = max(max_profit, p-lowest)
        return max_profit

    def maxProfit1(self, prices: List[int]) -> int:
        # mono stack
        s = []
        res = 0
        for n in prices:
            while s and n <= s[-1]:
                s.pop()
            s.append(n)
            if len(s) >= 2:
                res = max(res, s[-1]-s[0])
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        self.assertEqual(sol.maxProfit(prices), expected)

    def test_case_2(self):
        sol = Solution()
        prices = [7, 6, 4, 2, 1]
        expected = 0
        self.assertEqual(sol.maxProfit(prices), expected)

    def test_edge_case_1(self):
        sol = Solution()
        prices = [1]
        expected = 0
        self.assertEqual(sol.maxProfit(prices), expected)


if __name__ == "__main__":
    unittest.main()
