import unittest
from typing import List
from pprint import pprint

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        H,W = len(matrix),len(matrix[0])
        l = 0
        r = H*W-1
        while l <= r:
            mid = (l+r)>>1
            row,col = divmod(mid, W)
            m = matrix[row][col]
            if m == target:
                return True
            if m > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 3
        expected = True
        self.assertEqual(sol.searchMatrix(matrix, target), expected)

    def test_case_2(self):
        sol = Solution()
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 13
        expected = False
        self.assertEqual(sol.searchMatrix(matrix, target), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
