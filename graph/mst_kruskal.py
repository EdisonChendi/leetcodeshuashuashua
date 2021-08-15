import unittest
from typing import List, Union
from pprint import pprint

from unionfind import UnionFind
import heapq
from heapq import heappush, heappop


def mst_kruskal(graph):
    N = 5  # number of nodes
    h = []
    for e, w in graph.items():
        heappush(h, (w, e))
    mst = []
    uf = UnionFind(5)
    while True:
        _, edge = heappop(h)
        src, dst = edge
        isrc, idst = ord(src)-ord('A'), ord(dst)-ord('A')
        if uf.find_root(isrc) != uf.find_root(idst):
            uf.union(isrc, idst)
            mst.append(edge)
            if len(mst) == N-1:
                return mst


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        # sol = Solution()
        # graph = {
        #     'A': {
        #         'B': 0.5,
        #         'E': 1,
        #     },
        #     'B': {
        #         'A': 0.5,
        #         'C': 4,
        #         'D': 3,
        #         'E': 1.5,
        #     },
        #     'C': {
        #         'B': 4
        #     },
        #     'D': {
        #         'B': 3,
        #         'E': 2
        #     },
        #     'E': {
        #         'A': 1,
        #         'B': 1.5,
        #         'D': 2
        #     }
        # }
        graph = {
            'AB': 0.5,
            'AE': 1,
            'BE': 1.5,
            'BD': 3,
            'DE': 2,
            'BC': 4
        }
        mst = mst_kruskal(graph)
        print(mst)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
