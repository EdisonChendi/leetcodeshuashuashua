import unittest
from typing import List, Union
from pprint import pprint

from heapq import heappush, heappop


def manhattan_distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # to construct weights
        N = len(points)
        if N == 1:
            return 0

        all_nodes = set(range(N))
        visited = set()
        q = [(0, 0)]
        total_weight = 0

        while len(visited) < N:
            w, n = heappop(q)
            if n in visited:
                continue
            visited.add(n)
            total_weight += w
            for i in all_nodes-visited:
                heappush(q, (manhattan_distance(points[i], points[n]), i))

        return total_weight


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        points = [[3, 12], [-2, 5], [-4, 1]]
        expected = 18
        self.assertEqual(sol.minCostConnectPoints(points), expected)

    def test_case_2(self):
        sol = Solution()
        points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
        expected = 4
        self.assertEqual(sol.minCostConnectPoints(points), expected)

    def test_case_3(self):
        sol = Solution()
        points = [[-1000000, -1000000], [1000000, 1000000]]
        expected = 4000000
        self.assertEqual(sol.minCostConnectPoints(points), expected)

    def test_case_4(self):
        sol = Solution()
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        expected = 20
        self.assertEqual(sol.minCostConnectPoints(points), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
