import unittest
from typing import List
from pprint import pprint

# Big assumption of Dijkstra's shortest algorithm: # no negative weight path
# negative-weight edge paths -> Bellman-Ford can
# note: graph with negative weight cycle does NOT have shortest path solution
# (intuition: go through the negative weight cycle again, the path just get "shorter")


# Bellman-Form algorithm - a DP solution
# the shortest path - at MOST N-1 edges
# given a src
# dp[k][dst] - use at most k edges, shortest path from src 2 dst
# dp[k][dst] = min(dp[k-1][node] for all edge{node,dst})

import math
import collections


class ShortestPathBellmanFord:

    def solve(self, graph, src):
        def reverse_graph(graph):
            res = collections.defaultdict(dict)
            for src, dsts in graph.items():
                for dst, wei in dsts.items():
                    res[dst][src] = wei
            return res

        N = len(graph)
        dp = [math.inf]*N
        dp[src] = 0
        reversed_graph = reverse_graph(graph)
        for _ in range(1, N):
            new_dp = dp[:]
            for dst in range(N):
                for s, w in reversed_graph[dst].items():
                    new_dp[dst] = min(new_dp[dst], w+dp[s])
            dp = new_dp
        return dp


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        bellmanford = ShortestPathBellmanFord()
        graph = {
            0: {
                1: 100,
                2: 500,
                3: 200,
            },
            1: {
                2: 100,
            },
            2: {
                3: 100,
            },
            3: {
                1: -150,
            }
        }
        src = 0
        expected = [0, 50, 150, 200]
        res = bellmanford.solve(graph, src)
        self.assertListEqual(expected, res)


if __name__ == "__main__":
    unittest.main()
