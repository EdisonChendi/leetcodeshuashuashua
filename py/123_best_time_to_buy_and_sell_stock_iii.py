import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at most twice
        # state: 1.transaction count 2. holding or not
        # dp[c][h]
        # c in {0, 1}
        # h in {0, 1}, 0 not holding, 1 holding
        # dp transition:
        # dp[0][0] --buy--> dp[0][1]
        # dp[0][1] --sell--> dp[1][0]
        # dp[1][0] --buy--> dp[1][1]
        # dp[1][1] --sell--> cur_max
        dp = [[0, -math.inf], [-math.inf, -math.inf]]
        cur_max = 0
        for p in prices:
            dp[0][1] = max(dp[0][0]-p, dp[0][1])
            dp[1][0] = max(dp[0][1]+p, dp[1][0])
            dp[1][1] = max(dp[1][0]-p, dp[1][1])
            cur_max = max(dp[1][1]+p, cur_max)
        return cur_max


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        expected = 6
        self.assertEqual(sol.maxProfit(prices), expected)

    def test_case_2(self):
        sol = Solution()
        prices = [1, 2, 3, 4, 5]
        expected = 4
        self.assertEqual(sol.maxProfit(prices), expected)

    def test_case_3(self):
        sol = Solution()
        prices = [7, 6, 4, 3, 1]
        expected = 0
        self.assertEqual(sol.maxProfit(prices), expected)

    def test_case_4(self):
        sol = Solution()
        prices = [1]
        expected = 0
        self.assertEqual(sol.maxProfit(prices), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
