from math import exp
import unittest
from typing import List
from pprint import pprint
import math
from heapq import heappop, heappush
from collections import defaultdict
from shortest_path_dijkstra import ShortestPathDijkstra


class Solution:
    def networkDelayTime1(self, times: List[List[int]], n: int, k: int) -> int:
        def build_graph(times, n):
            graph = {i: {} for i in range(1, n+1)}
            for src, dst, weight in times:
                graph[src][dst] = weight
            return graph
        graph = build_graph(times, n)
        shortest_paths = ShortestPathDijkstra().solve(graph, k)
        res = max(item[0] for _, item in shortest_paths.items())
        return res if res != math.inf else -1

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def build_graph(times, n):
            graph = {i: [] for i in range(1, n+1)}
            for src, dst, weight in times:
                graph[src].append((dst, weight))
            return graph

        N = n
        graph = build_graph(times, N)
        h = [(0, k), ]
        res = {}
        while h:
            d, n = heappop(h)
            if n in res:
                continue
            res[n] = d
            for nei, weight in graph[n]:
                if nei in res:
                    continue
                heappush(h, (weight+d, nei))
        return max(res.values()) if len(res) == N else -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        expected = 2
        self.assertEqual(sol.networkDelayTime(times, n, k), expected)

    def test_case_2(self):
        sol = Solution()
        times = [[1, 2, 1]]
        n = 2
        k = 1
        expected = 1
        self.assertEqual(sol.networkDelayTime(times, n, k), expected)

    def test_case_3(self):
        sol = Solution()
        times = [[1, 2, 1]]
        n = 2
        k = 2
        expected = -1
        self.assertEqual(sol.networkDelayTime(times, n, k), expected)

    def test_case_4(self):
        sol = Solution()
        times = [[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]]
        n = 4
        k = 1
        expected = -1
        self.assertEqual(sol.networkDelayTime(times, n, k), expected)

    def test_case_5(self):
        sol = Solution()
        times = [[2, 4, 10], [5, 2, 38], [3, 4, 33], [4, 2, 76], [3, 2, 64], [1, 5, 54], [1, 4, 98], [2, 3, 61], [2, 1, 0], [3, 5, 77], [
            5, 1, 34], [3, 1, 79], [5, 3, 2], [1, 2, 59], [4, 3, 46], [5, 4, 44], [2, 5, 89], [4, 5, 21], [1, 3, 86], [4, 1, 95]]
        n = 5
        k = 1
        expected = 69
        self.assertEqual(sol.networkDelayTime(times, n, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
