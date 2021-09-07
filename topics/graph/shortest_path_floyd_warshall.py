import unittest
from typing import List
from pprint import pprint
from copy import deepcopy
from math import inf


class FloydWarshall:

    def solve(self, graph):
        N = len(graph)
        dp = [[0, ]*N for _ in range(N)]
        paths = [[-2, ]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                w = graph[i][j]
                dp[i][j] = w
                if w != inf:
                    paths[i][j] = j

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    through_k = dp[i][k]+dp[k][j]
                    if through_k < dp[i][j]:
                        dp[i][j] = through_k
                        paths[i][j] = paths[i][k]

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    through_k = dp[i][k]+dp[k][j]
                    if through_k < dp[i][j]:
                        dp[i][j] = -inf
                        paths[i][j] = -1

        return dp, paths

    @staticmethod
    def find_path(paths, src, dst):
        pass


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        print("-"*50)
        algo = FloydWarshall()
        graph = [
            [0, 4, 1, 9],
            [3, 0, 6, 11],
            [4, 1, 0, 2],
            [6, 5, 4, 0]
        ]
        dists, paths = algo.solve(graph)
        print("shortest path between all node pairs:")
        pprint(dists)
        print("construct the path:")
        pprint(paths)
        # print(algo.find_path(paths, 'D', 'A'))

    def test_case_2(self):
        print("-"*50)
        algo = FloydWarshall()
        graph = [
            [0, 4, inf, inf, inf, inf, 2],
            [inf, -1, 3, inf, inf, inf, inf],
            [inf, inf, 0, 3, 1, inf, inf],
            [inf, inf, inf, 0, inf, -2, inf],
            [inf, inf, inf, inf, 0, 2, inf],
            [inf, inf, inf, inf, inf, 0, inf],
            [inf, inf, inf, inf, 2, inf, inf]
        ]
        dists, paths = algo.solve(graph)
        print("shortest path between all node pairs:")
        pprint(dists)
        print("construct the path:")
        pprint(paths)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
