import unittest
from typing import List
from pprint import pprint


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))

    def find_root(self, i):
        root = i
        while root != self.parent[root]:
            root = self.parent[root]
        while i != self.parent[i]:
            self.parent[i], i = root, self.parent[i]
        return root

    def union(self, i, j):
        root_i = self.find_root(i)
        root_j = self.find_root(j)
        if root_i == root_j:
            return
        self.parent[root_i] = root_j


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        uf = UnionFind(5)
        self.assertTrue(uf.find_root(1), 1)
        self.assertTrue(uf.find_root(2), 2)
        uf.union(1, 2)
        uf.union(2, 3)
        self.assertEqual(uf.find_root(1), uf.find_root(2))
        self.assertEqual(uf.find_root(3), uf.find_root(2))
        self.assertNotEqual(uf.find_root(1), uf.find_root(4))

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
