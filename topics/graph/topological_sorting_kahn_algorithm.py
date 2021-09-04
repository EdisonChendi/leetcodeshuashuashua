import unittest
from typing import List
from pprint import pprint
import collections


class TopologicalSortingKahnAlgorithm:

    def solve(self, graph):
        def cal_in_degrees(graph):
            res = {n: 0 for n in graph}
            for _, dsts in graph.items():
                for n in dsts:
                    res[n] += 1
            return res

        res = []
        in_degrees = cal_in_degrees(graph)
        q = collections.deque(n for n, d in in_degrees.items() if d == 0)
        while q:
            n = q.popleft()
            res.append(n)
            for dst in graph[n]:
                in_degrees[dst] -= 1
                if in_degrees[dst] == 0:
                    q.append(dst)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        algo = TopologicalSortingKahnAlgorithm()
        graph = {
            'A': ('B', 'C'),
            'B': ('D'),
            'C': ('B', 'D'),
            'D': ()
        }
        expected = ['A', 'C', 'B', 'D']
        res = algo.solve(graph)
        self.assertListEqual(expected, res)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
