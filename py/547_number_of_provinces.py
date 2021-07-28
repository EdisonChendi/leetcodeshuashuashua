import unittest
from typing import List
from pprint import pprint


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

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
        self.count -= 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # by dfs
        def dfs(i):
            for j in range(N):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = 0
                    dfs(j)

        N, count = len(isConnected), 0
        for i in range(N):
            if isConnected[i][i] == 1:
                isConnected[i][i] = 0
                dfs(i)
                count += 1
            
        return count

    def findCircleNum1(self, isConnected: List[List[int]]) -> int:
        # by union find
        N = len(isConnected)
        uf = UnionFind(N)
        for i in range(N):
            for j in range(i+1, N):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.count


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        expected = 2
        self.assertEqual(sol.findCircleNum(isConnected), expected)

    def test_case_2(self):
        sol = Solution()
        isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        expected = 3
        self.assertEqual(sol.findCircleNum(isConnected), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
