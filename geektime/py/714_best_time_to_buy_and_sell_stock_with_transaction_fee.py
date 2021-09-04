import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        holding, not_holding = -prices[0], 0
        for p in prices[1:]:
            holding = max(holding, not_holding-p)
            not_holding = max(not_holding, holding+p-fee)
        return not_holding


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        prices = [1, 3, 2, 8, 4, 9]
        fee = 2
        expected = 8
        self.assertEqual(sol.maxProfit(prices, fee), expected)

    def test_case_2(self):
        sol = Solution()
        prices = [1, 3, 7, 5, 10, 3]
        fee = 3
        expected = 6
        self.assertEqual(sol.maxProfit(prices, fee), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
