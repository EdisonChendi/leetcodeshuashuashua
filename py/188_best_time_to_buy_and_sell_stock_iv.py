import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # dp[transaction_count][not holding/holding] = profit
        if k == 0 or len(prices) <= 1:
            return 0

        dp = [[-math.inf, -math.inf] for _ in range(k)]
        dp[0][0], profit = 0, 0
        for p in prices:
            for j in range(k):
                dp[j][0] = max(dp[j][0], dp[j-1][1]+p) if j > 0 else dp[j][0]
                dp[j][1] = max(dp[j][1], dp[j][0]-p)
            profit = max(profit, dp[-1][-1]+p)
        return profit


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        k = 2
        prices = [2, 4, 1]
        expected = 2
        self.assertEqual(sol.maxProfit(k, prices), expected)

    def test_case_2(self):
        sol = Solution()
        k = 2
        prices = [3, 2, 6, 5, 0, 3]
        expected = 7
        self.assertEqual(sol.maxProfit(k, prices), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
