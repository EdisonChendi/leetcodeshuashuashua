import unittest
from typing import List
from pprint import pprint
import collections
import math


class Solution:

    def top_sort(self, edges, nodes):
        # V - num of vertices(nodes)
        # E - num of edges
        # O(V+E)
        ins = collections.defaultdict(set)
        outs = collections.defaultdict(set)
        for s, d, _ in edges:
            outs[s].add(d)
            ins[d].add(s)

        res = []
        q = [n for n in nodes if len(ins[n]) == 0]
        while q:
            nxt = []
            while q:
                node = q.pop()
                res.append(node)
                for nei in outs[node]:
                    ins[nei].remove(node)
                    if len(ins[nei]) == 0:
                        nxt.append(nei)
            q = nxt
        return res

    def sssp_dag(self, edges, start):
        adjlists = collections.defaultdict(dict)
        nodes = set()
        for s, d, w in edges:
            adjlists[s][d] = w
            nodes.add(s)
            nodes.add(d)

        res = {n: math.inf for n in nodes}
        res[start] = 0

        top_sorted = self.top_sort(edges, nodes)

        for n in top_sorted:
            for nei, w in adjlists[n].items():
                res[nei] = min(res[nei], res[n]+w)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        edges = [('A', 'B', 3),
                 ('A', 'C', 6),
                 ('B', 'C', 4),
                 ('B', 'D', 4),
                 ('C', 'D', 8),
                 ('C', 'G', 11),
                 ('B', 'E', 11),
                 ('D', 'E', -4),
                 ('D', 'F', 5),
                 ('D', 'G', 2),
                 ('E', 'H', 9),
                 ('F', 'H', 1),
                 ('G', 'H', 2)]
        res = sol.sssp_dag(edges, 'A')
        print(sorted(res.items()))

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
