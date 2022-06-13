import unittest
from typing import List
from pprint import pprint
from heapq import heappush, heappop
from collections import defaultdict


class Solution:

    def prim(self, edges, n):
        # greedy
        # O(ElgE)
        def add_edges(idx):
            visited.add(idx)
            for nei, w in adjlists[idx].items():
                if nei not in visited:
                    heappush(h, (w, idx, nei))

        def to_adjlists(edges):
            adjlists = defaultdict(dict)
            for s, d, w in edges:
                adjlists[s][d] = w
                adjlists[d][s] = w
            return adjlists

        starting = 0
        h = [(0, -1, starting)]
        visited = set()
        adjlists = to_adjlists(edges)
        cnt = 0
        cost = 0
        trees = []
        while h and cnt < n:
            w, s, d = heappop(h)
            if d in visited:  # lazy heap
                continue
            cost += w
            cnt += 1
            trees.append((s, d, w))
            add_edges(d)

        return cost, trees[1:]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        edges = [
            (0, 1, 5),
            (1, 2, 4),
            (2, 9, 2),
            (0, 4, 1),
            (0, 3, 4),
            (1, 3, 2),
            (2, 7, 4),
            (2, 8, 1),
            (9, 8, 0),
            (4, 5, 1),
            (5, 6, 7),
            (6, 8, 4),
            (4, 3, 2),
            (5, 3, 5),
            (3, 6, 11),
            (6, 7, 1),
            (3, 7, 2),
            (7, 8, 6)
        ]
        n = 10
        expected = 14
        res_cost, res_trees = sol.prim(edges, n)
        print(res_trees)
        self.assertEqual(res_cost, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
