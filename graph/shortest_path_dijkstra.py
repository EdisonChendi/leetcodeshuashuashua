import unittest
from typing import List
from pprint import pprint
from heapq import heappop, heappush, _siftdown
from math import inf


class ShortestPathDijkstra:

    def solve(self, graph, src):
        N = len(graph)
        res = {}  # visited
        h = []

        for n in graph:
            heappush(h, (inf if n != src else 0, n, None))

        while len(res) < N:
            # step 1 - find node with shortest path
            d, node, parent = heappop(h)
            res[node] = (d, parent)

            # step 2 - do relaxation
            relaxation = {}
            for nei, btw in graph[node].items():
                if nei not in res:
                    relaxation[nei] = d+btw

            # step 3 - update the heap (better than rebuild heap)
            cur_parent = node
            for i, ele in enumerate(h):
                d, node, parent = ele
                if node in relaxation and relaxation[node] < d:
                    h[i] = (relaxation[node], node, cur_parent)
                    _siftdown(h, 0, i)

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        dijkstra = ShortestPathDijkstra()
        graph = {
            'A': {
                'B': 1,
                'C': 1,
                'D': 3,
            },
            'B': {
                'A': 1,
                'D': 2,
                'E': 1,
            },
            'C': {
                'A': 1,
                'D': 1
            },
            'D': {
                'A': 3,
                'B': 2,
                'C': 1,
                'E': 2,
            },
            'E': {
                'B': 1,
                'D': 2,
            }
        }
        src = 'A'
        res = dijkstra.solve(graph, src)
        expected = {
            'A': (0, None),
            'B': (1, 'A'),
            'C': (1, 'A'),
            'D': (2, 'C'),
            'E': (2, 'B'),
        }
        self.assertDictEqual(res, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
