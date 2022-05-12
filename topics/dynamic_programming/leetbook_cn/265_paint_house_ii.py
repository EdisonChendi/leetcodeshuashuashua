import math

import unittest
from typing import List
from pprint import pprint


class Solution1:
    def minCostII(self, costs: List[List[int]]) -> int:
        N, K = len(costs), len(costs[0])
        dp = [0]*K
        for i in range(N):
            nxt_dp = [0]*K
            for clr, cost in enumerate(costs[i]):
                nxt_dp[clr] = cost + \
                    min(c for i, c in enumerate(dp) if i != clr)
            dp = nxt_dp
        return min(dp)


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        N, K = len(costs), len(costs[0])
        m1 = m2 = 0
        idx = -1
        for i in range(N):
            mm1, mm2, iidx = math.inf, math.inf, -1
            for clr, c in enumerate(costs[i]):
                clr_c = c + (m1 if clr != idx else m2)
                if clr_c <= mm1 <= mm2:
                    mm1, mm2 = clr_c, mm1
                    iidx = clr
                elif mm1 <= clr_c <= mm2:
                    mm1, mm2 = mm1, clr_c
            m1, m2, idx = mm1, mm2, iidx
        return m1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        costs = [[1, 5, 3], [2, 9, 4]]
        expected = 5
        self.assertEqual(sol.minCostII(costs), expected)

    def test_case_2(self):
        sol = Solution()
        costs = [[1, 3], [2, 4]]
        expected = 5
        self.assertEqual(sol.minCostII(costs), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
