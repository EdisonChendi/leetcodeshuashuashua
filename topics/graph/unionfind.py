import unittest
from typing import List
from pprint import pprint


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    # def find_root(self, i):
    #     # find by compression
    #     root = i
    #     while root != self.parent[root]:
    #         root = self.parent[root]
    #     while i != root:
    #         self.parent[i], i = root, self.parent[i]
    #     return root

    def find_root(self, i):
        if i == self.parent[i]:
            return i
        self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find_root(i)
        root_j = self.find_root(j)
        if root_i == root_j:
            return False
        self.parent[root_j] = root_i
        self.count -= 1
        return True

    def connected(self, i, j):
        return self.find_root(i) == self.find_root(j)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        # Test Case
        uf = UnionFind(10)
        # 1-2-5-6-7 3-8-9 4
        uf.union(1, 2)
        uf.union(2, 5)
        uf.union(5, 6)
        uf.union(6, 7)
        uf.union(3, 8)
        uf.union(8, 9)

        self.assertEqual(uf.connected(1, 5), True)
        self.assertEqual(uf.connected(5, 7), True)
        self.assertEqual(uf.connected(4, 9), False)
        # 1-2-5-6-7 3-8-9-4
        uf.union(9, 4)
        self.assertEqual(uf.connected(4, 9), True)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
