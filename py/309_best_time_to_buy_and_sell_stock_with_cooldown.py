import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, cool, sell = -prices[0], 0, 0
        for p in prices[1:]:
            buy, cool, sell = max(buy, cool-p), max(cool,
                                                    sell), max(sell, buy+p)
        return sell


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        prices = [1, 2, 3, 0, 2]
        expected = 3
        self.assertEqual(sol.maxProfit(prices), expected)

    def test_case_2(self):
        sol = Solution()
        prices = [1]
        expected = 0
        self.assertEqual(sol.maxProfit(prices), expected)

    def test_case_3(self):
        sol = Solution()
        prices = [2, 1, 4]
        expected = 3
        self.assertEqual(sol.maxProfit(prices), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
