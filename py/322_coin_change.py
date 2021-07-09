import unittest
from typing import List
from pprint import pprint
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0,] + [math.inf,]*amount
        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], 1+dp[i-c])
        return dp[-1] if dp[-1] != math.inf else -1
        

    def coinChange1(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = {0}
        count = 0
        while dp:
            count += 1
            new_dp = set()
            for c in coins:
                for v in dp:
                    n = c+v
                    if n > amount: continue
                    if n == amount: return count
                    if n not in dp: new_dp.add(n)
            dp = new_dp
        return -1

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        coins = [1,2,5]; amount = 11
        expected = 3
        self.assertEqual(sol.coinChange(coins, amount), expected)

    def test_case_2(self):
        sol = Solution()
        coins = [2]; amount = 3
        expected = -1
        self.assertEqual(sol.coinChange(coins, amount), expected)

    def test_case_3(self):
        sol = Solution()
        coins = [1]; amount = 0
        expected = 0
        self.assertEqual(sol.coinChange(coins, amount), expected)
        
    def test_case_4(self):
        sol = Solution()
        coins = [1]; amount = 1
        expected = 1
        self.assertEqual(sol.coinChange(coins, amount), expected)

    def test_case_5(self):
        sol = Solution()
        coins = [1]; amount = 2
        expected = 2
        self.assertEqual(sol.coinChange(coins, amount), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
