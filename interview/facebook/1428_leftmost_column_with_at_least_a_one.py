import unittest
from typing import List
from pprint import pprint


class BinaryMatrix(object):
    def __init__(self, matrix) -> None:
        self.mat = matrix

    def get(self, row: int, col: int) -> int:
        return self.mat[row][col]

    def dimensions(self):
        return [len(self.mat), len(self.mat[0])]


class Solution1:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # binary search
        def binary_search(row, l, r):
            while l <= r:
                mid = (l+r) >> 1
                n = binaryMatrix.get(row, mid)
                if n == 0:
                    l = mid+1
                else:
                    r = mid-1
            return l

        H, W = binaryMatrix.dimensions()
        res = W
        for r in range(H):
            res = min(res, binary_search(r, 0, W-1))
        return -1 if res == W else res


class Solution2:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # binary search
        def binary_search(row, l, r):
            while l <= r:
                mid = (l+r) >> 1
                n = binaryMatrix.get(row, mid)
                if n == 0:
                    l = mid+1
                else:
                    r = mid-1
            return l

        H, W = binaryMatrix.dimensions()
        res = W
        for r in range(H):
            if binaryMatrix.get(r, res-1) == 1:
                res = min(res, binary_search(r, 0, res-1))
                if res == 0:
                    return res
        return -1 if res == W else res


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # O(N+M)
        H, W = binaryMatrix.dimensions()
        res = W
        for r in range(H):
            while res > 0 and binaryMatrix.get(r, res-1) == 1:
                res = res-1
            if res == 0:
                return res
        return -1 if res == W else res


class TestSolution(unittest.TestCase):

    def test_case_0(self):
        sol = Solution()
        mat = BinaryMatrix([[0, 0], [1, 1]])
        expected = 0
        self.assertEqual(sol.leftMostColumnWithOne(mat), expected)

    def test_case_1(self):
        sol = Solution()
        mat = BinaryMatrix([[0, 0], [0, 1]])
        expected = 1
        self.assertEqual(sol.leftMostColumnWithOne(mat), expected)

    def test_case_2(self):
        sol = Solution()
        mat = BinaryMatrix([[0, 0], [0, 0]])
        expected = -1
        self.assertEqual(sol.leftMostColumnWithOne(mat), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
