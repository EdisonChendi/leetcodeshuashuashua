import unittest
from typing import List
from pprint import pprint


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # assert m > 0 and n > 0

        l, r = 0, m*n-1
        while l <= r:
            mid = (l+r) >> 1
            v = matrix[mid//n][mid % n]
            if v == target:
                return True
            l, r = (l, mid-1) if v > target else (mid+1, r)
        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        expected = True
        self.assertEqual(sol.searchMatrix(matrix, target), expected)

    def test_case_2(self):
        sol = Solution()
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        expected = False
        self.assertEqual(sol.searchMatrix(matrix, target), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
