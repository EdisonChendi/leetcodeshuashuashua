import unittest
from typing import List
from pprint import pprint


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(days[-1]+1)
        days = set(days)
        for d in range(1, len(dp)):
            if d not in days:
                dp[d] = dp[d-1]
            else:
                dp[d] = min(
                    dp[d-1]+costs[0],
                    (dp[d-7] if d >= 7 else 0) + costs[1],
                    (dp[d-30] if d >= 30 else 0) + costs[2]
                )
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
