from math import exp
import unittest
from typing import List
from pprint import pprint


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1, ]+[0]*amount
        for c in coins:
            for v in range(c, len(dp)):
                dp[v] += dp[v-c]
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        amount = 5
        coins = [1, 2, 5]
        expected = 4
        self.assertEqual(sol.change(amount, coins), expected)

    def test_case_2(self):
        sol = Solution()
        amount = 3
        coins = [2]
        expected = 0
        self.assertEqual(sol.change(amount, coins), expected)

    def test_case_3(self):
        sol = Solution()
        amount = 10
        coins = [10]
        expected = 1
        self.assertEqual(sol.change(amount, coins), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
