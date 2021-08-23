import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack = []
        visit = [0, ]*numCourses  # 0 unvisited | 1 visiting | 2 visited
        graph = {i: [] for i in range(numCourses)}
        for dst, src in prerequisites:
            graph[src].append(dst)

        def dfs(node):
            if visit[node] == 2:
                return

            if visit[node] == 1:
                raise

            visit[node] = 1
            for dst in graph[node]:
                dfs(dst)

            visit[node] = 2
            stack.append(node)

        try:
            for node in range(numCourses):
                dfs(node)
            return stack[::-1]
        except:
            return []


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [0, 1]
        res = sol.findOrder(numCourses, prerequisites)
        self.assertEqual(expected, res)

    def test_case_2(self):
        sol = Solution()
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        expected = [0, 2, 1, 3]
        res = sol.findOrder(numCourses, prerequisites)
        self.assertEqual(expected, res)

    def test_case_3(self):
        sol = Solution()
        numCourses = 1
        prerequisites = []
        expected = [0]
        res = sol.findOrder(numCourses, prerequisites)
        self.assertEqual(expected, res)

    def test_case_4(self):
        sol = Solution()
        numCourses = 4
        prerequisites = [[1, 0], [2, 1], [0, 2], [3, 0]]
        expected = []
        res = sol.findOrder(numCourses, prerequisites)
        self.assertEqual(expected, res)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
