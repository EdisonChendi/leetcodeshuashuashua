from math import remainder
import unittest
from typing import List
from pprint import pprint

import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        adjlists = collections.defaultdict(set)
        for f, t in edges:
            adjlists[f].add(t)
            adjlists[t].add(f)

        remain = n
        leaves = [i for i, neis in adjlists.items() if len(neis) <= 1]
        while remain > 2:
            remain -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                target = adjlists[leaf].pop()
                adjlists[target].remove(leaf)
                if len(adjlists[target]) == 1:
                    new_leaves.append(target)
            leaves = new_leaves
        return leaves


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 4
        edges = [[1, 0], [1, 2], [1, 3]]
        expected = [1]
        self.assertCountEqual(sol.findMinHeightTrees(n, edges), expected)

    def test_case_2(self):
        sol = Solution()
        n = 6
        edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
        expected = [3, 4]
        self.assertCountEqual(sol.findMinHeightTrees(n, edges), expected)


if __name__ == "__main__":
    unittest.main()
