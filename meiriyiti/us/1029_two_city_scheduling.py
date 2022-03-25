import unittest
from typing import List
from pprint import pprint


# dp[i][j] == min(dp[i-1][j]+costs[k][0], dp[i][j-1]+costs[k][1])
# return dp[-1][-1]

class Solution1:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        dp = [[0]*(N+1) for _ in range(N+1)]
        for i in range(1, N+1):
            a, b = costs[i-1]
            dp[i][0] = dp[i-1][0] + a
            dp[0][i] = dp[0][i-1] + b
            for j in range(1, i):
                dp[j][i-j] = min(dp[j-1][i-j]+a, dp[j][i-j-1]+b)
        return dp[N//2][N//2]


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)//2
        costs.sort(key=lambda c: c[0]-c[1])
        return sum(costs[i][0] + costs[i+N][1]for i in range(N))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
        expected = 110
        self.assertEqual(sol.twoCitySchedCost(costs), expected)

    def test_case_2(self):
        sol = Solution()
        costs = [[259, 770], [448, 54], [926, 667],
                 [184, 139], [840, 118], [577, 469]]
        expected = 1859
        self.assertEqual(sol.twoCitySchedCost(costs), expected)

    def test_case_3(self):
        sol = Solution()
        costs = [[515, 563], [451, 713], [537, 709], [343, 819],
                 [855, 779], [457, 60], [650, 359], [631, 42]]
        expected = 3086
        self.assertEqual(sol.twoCitySchedCost(costs), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
