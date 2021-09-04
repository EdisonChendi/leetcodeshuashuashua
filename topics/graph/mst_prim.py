import unittest
from typing import List, Union
from pprint import pprint

from unionfind import UnionFind
from heapq import heappush, heappop
import random


def mst_prim(graph):
    N = len(graph)
    res = []
    total_weight = 0
    q = []
    visited = set()
    nodes = list(graph.keys())
    first = random.choice(nodes)
    heappush(q, (0, '', first))

    while len(visited) < N:
        w, l, n = heappop(q)
        if n in visited:
            continue
        visited.add(n)
        res.append(l+n)
        total_weight += w
        for dst, weight in graph[n].items():
            if dst not in visited:
                heappush(q, (weight, n, dst))

    return res, total_weight


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        graph = {
            'A': {
                'B': 0.5,
                'E': 1,
            },
            'B': {
                'A': 0.5,
                'C': 4,
                'D': 3,
                'E': 1.5,
            },
            'C': {
                'B': 4
            },
            'D': {
                'B': 3,
                'E': 2
            },
            'E': {
                'A': 1,
                'B': 1.5,
                'D': 2
            }
        }
        mst = mst_prim(graph)
        print(mst)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
