import unittest
from typing import List
from pprint import pprint

import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        for amt in range(1, len(dp)):
            dp[amt] = 1+min((dp[amt-c]
                            for c in coins if amt - c >= 0), default=math.inf)
        return dp[amount] if dp[amount] < math.inf else -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
