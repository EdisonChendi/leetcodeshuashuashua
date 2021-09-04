import unittest
from typing import List
from pprint import pprint


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(n, accu, visited, res):
            if n == len(graph)-1:
                res.append(accu[:])
                return res

            for nei in graph[n]:
                if nei not in visited:
                    visited.add(nei)
                    accu.append(nei)
                    dfs(nei, accu, visited, res)
                    accu.pop()
                    visited.remove(nei)

            return res

        return dfs(0, [0, ], {0}, [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        graph = [[1, 2], [3], [3], []]
        expected = [[0, 1, 3], [0, 2, 3]]
        self.assertCountEqual(sol.allPathsSourceTarget(graph), expected)

    def test_case_2(self):
        sol = Solution()
        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        expected = [[0, 4], [0, 3, 4], [
            0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
        self.assertCountEqual(sol.allPathsSourceTarget(graph), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
