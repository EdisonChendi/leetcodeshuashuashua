from enum import IntEnum
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        na = {}
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                k = i-j
                if k not in na:
                    na[k] = n
                elif na[k] != n:
                    return False
        return True


class Solution2:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        H, W = len(matrix), len(matrix[0])
        for i in range(1, H):
            for j in range(1, W):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r == 0 or c == 0 or n == matrix[r-1][c-1] for r, row in enumerate(matrix) for c, n in enumerate(row))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
        expected = True
        self.assertEqual(sol.isToeplitzMatrix(matrix), expected)

    def test_case_2(self):
        sol = Solution()
        matrix = [[1, 2], [2, 2]]
        expected = False
        self.assertEqual(sol.isToeplitzMatrix(matrix), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
