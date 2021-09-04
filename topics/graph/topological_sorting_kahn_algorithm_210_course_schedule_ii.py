import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def helper(numCourses,  prerequisites):
            graph = {i: [] for i in range(numCourses)}
            indgrees = [0, ]*numCourses
            for dst, src in prerequisites:
                graph[src].append(dst)
                indgrees[dst] += 1
            return graph, indgrees

        graph, indgrees = helper(numCourses, prerequisites)
        res = []
        q = collections.deque(n for n, d in enumerate(indgrees) if d == 0)
        while q:
            n = q.popleft()
            res.append(n)
            for dst in graph[n]:
                indgrees[dst] -= 1
                if indgrees[dst] == 0:
                    q.append(dst)
        return res if len(res) == numCourses else []


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
        expected = [0, 1, 2, 3]
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
