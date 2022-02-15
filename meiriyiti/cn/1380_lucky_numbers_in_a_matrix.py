import unittest
from typing import List
from pprint import pprint
import math


class Solution1:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        H, W = len(matrix), len(matrix[0])
        row_min = [math.inf, ]*H
        col_max = [0]*W
        for i in range(H):
            for j in range(W):
                row_min[i] = min(row_min[i], matrix[i][j])
                col_max[j] = max(col_max[j], matrix[i][j])
        res = []
        for i in range(H):
            for j in range(W):
                if row_min[i] == matrix[i][j] == col_max[j]:
                    res.append(matrix[i][j])
        return res


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]
        res = []
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if row_min[i] == n == col_max[j]:
                    res.append(n)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
        expected = [15]
        self.assertListEqual(sol.luckyNumbers(matrix), expected)

    def test_case_2(self):
        sol = Solution()
        matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
        expected = [12]
        self.assertListEqual(sol.luckyNumbers(matrix), expected)

    def test_case_3(self):
        sol = Solution()
        matrix = [[7, 8], [1, 2]]
        expected = [7]
        self.assertListEqual(sol.luckyNumbers(matrix), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
