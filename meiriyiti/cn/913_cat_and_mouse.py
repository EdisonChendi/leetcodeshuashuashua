import unittest
from typing import List
from pprint import pprint

import functools


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        """
        -1 - mouse wins - mouse wants to minimize dfs
        0  - draw game
        1  - cat wins - cat wants to maximize dfs
        """
        @functools.cache
        def dfs(m, c, r):
            if r >= 2*len(graph):
                return 0

            if m == 0:
                return -1
            if m == c:
                return 1

            res = (-1)**r
            if r % 2 == 0:
                # mouse move
                for nei in graph[m]:
                    res = min(res, dfs(nei, c, r+1))
                    if res == -1:
                        break
            else:
                for nei in graph[c]:
                    if nei == 0:
                        continue
                    res = max(res, dfs(m, nei, r+1))
                    if res == 1:
                        break
            return res

        if (ans := dfs(1, 2, 0)) == 0:
            return 0
        else:
            return 1 if ans == -1 else 2


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
        expected = 0
        self.assertEqual(sol.catMouseGame(graph), expected)

    def test_case_2(self):
        sol = Solution()
        graph = [[1, 3], [0], [3], [0, 2]]
        expected = 1
        self.assertEqual(sol.catMouseGame(graph), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
