import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cnt = collections.Counter()
        for s, d in edges[:2]:
            cnt[s] += 1
            cnt[d] += 1
        for node, n in cnt.items():
            if n == 2:
                return node


class Solution2:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = set()
        for s, d in edges:
            if s in nodes:
                return s
            if d in nodes:
                return d
            nodes.add(s)
            nodes.add(d)


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        edges = [[1, 2], [2, 3], [4, 2]]
        expected = 2
        self.assertEqual(sol.findCenter(edges), expected)

    def test_case_2(self):
        sol = Solution()
        edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
        expected = 1
        self.assertEqual(sol.findCenter(edges), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
