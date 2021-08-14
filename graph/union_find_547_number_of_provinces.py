import unittest
from typing import List
from pprint import pprint
from unionfind import UnionFind


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
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
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
