import unittest
from typing import List
from pprint import pprint

# Floyd-Marshall algorithm
# O(V2)
# All pair shortest path solution
# dynamic programming
# dp[k][i][j] - shortest path btw. i and j routing through 0..k
# dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k]+dp[k-1][k][j])

import math


class Solution:

    def apsp_floydmarshall(self, adj_matrix):
        dp = [r[:] for r in adj_matrix]
        N = len(dp)
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

        # detect negative cycles
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dp[i][j] > dp[i][k]+dp[k][j]:
                        dp[i][j] = -math.inf
        return dp


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        def make_adjmatrix(edges, N):
            m = [[math.inf]*N for _ in range(N)]
            for i in range(N):
                m[i][i] = 0
            for i, j, w in edges:
                m[i][j] = w
            return m

        sol = Solution()
        edges = [(0, 1, 2), (0, 2, 5), (0, 6, 10), (1, 2, 2),
                 (1, 4, 11), (2, 6, 2), (6, 5, 11), (4, 5, 1), (5, 4, -2)]
        adj_matrix = make_adjmatrix(edges, 7)
        # expected = []
        res = sol.apsp_floydmarshall(adj_matrix)
        print(res)
        # self.assertListEqual(expected, res)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
