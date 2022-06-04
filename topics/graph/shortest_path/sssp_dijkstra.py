import unittest
from typing import List
from pprint import pprint

import collections
import math
import heapq


class Solution:
    # use a normal binary heap + lazy
    # Dijkstra only works in graph with no negative values
    # greedy method
    # E - num of edges
    # V - num of vertices(nodes)
    # O(ElgV)

    def sssp_dijkstra(self, edges, start):
        nodes = set()
        adjlists = collections.defaultdict(dict)
        for s, d, w in edges:
            adjlists[s][d] = w
            nodes.update({s, d})

        N = len(nodes)
        res = [math.inf] * N
        res[start] = 0
        h = [(0, start)]

        while h:
            dist, node = heapq.heappop(h)
            if res[node] < dist:
                continue
            neighbors = adjlists[node]
            for nei, wei in neighbors.items():
                ndist = dist+wei
                if res[nei] > ndist:  # lazy
                    res[nei] = ndist
                    heapq.heappush(h, (ndist, nei))
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        edges = [(0, 1, 4),
                 (0, 2, 1),
                 (2, 1, 2),
                 (1, 3, 1),
                 (2, 3, 5),
                 (3, 4, 3)]
        start = 0
        res = sol.sssp_dijkstra(edges, start)
        expected = [0, 3, 1, 4, 7]
        self.assertListEqual(res, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
