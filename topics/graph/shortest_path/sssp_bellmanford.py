import unittest
from typing import List
from pprint import pprint


# Dijkstra can handle negative weights
# if negative weights is in the graph,
# it is possible to have nagative cycles
# which can results in -inf path weights
# by going through the negative cycles repeatedly
# --------------------------------------------------
# BellmanFord algorithm is able to handle negative cycles
# if there is no negative cycles
# it can give shortest path from a single node to every other node
# if there are some negative cycles
# it can detect negative cycles!

import collections
import math


class Solution:

    def sssp_bellmanford(self, edges, start):
        nodes = set()
        for s, d, w in edges:
            nodes.update({s, d})

        N = len(nodes)
        D = [math.inf]*N
        D[start] = 0
        P = list(range(N))
        for _ in range(N-1):
            # why N-1 here?
            # how many edges btw. two nodes(N nodes at most)
            # 1.2.3...k...N-2.N-1.N
            # => N-1 edges at most
            # 思考题：
            # 为什么edges顺序是无关紧要的？
            # https://leetcode.cn/leetbook/read/graph/rq3glc/
            # dp[k][u] = min(dp[k-1][v]+w(v,u)) for every v -> u
            # k - (at most) number of edges from start to u
            for s, d, w in edges:
                if D[s] + w < D[d]:
                    D[d] = D[s] + w
                    P[d] = s

        # negative cycle detection
        # below link: how to find the negative cycle
        # https://cp-algorithms.com/graph/finding-negative-cycle-in-graph.html#using-bellman-ford-algorithm
        for _ in range(N-1):
            for s, d, w in edges:
                if D[s] + w < D[d]:
                    D[d] = -math.inf
                    P[d] = s

        print(list(range(N)))
        print(D)
        print(P)
        return D


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        edges = [
            (0, 1, 5),
            (1, 6, 60),
            (1, 2, 20),
            (2, 3, 10),
            (3, 2, -15),
            (2, 4, 75),
            (1, 5, 30),
            (5, 6, 5),
            (6, 7, -50),
            (5, 4, 25),
            (7, 8, -10),
            (5, 8, 50),
            (4, 9, 100)
        ]
        start = 0
        res = sol.sssp_bellmanford(edges, start)
        expected = [0, 5, -math.inf, -math.inf, -math.inf,
                    35, 40, -10, -20, -math.inf]
        self.assertListEqual(res, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
