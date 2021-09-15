import unittest
from typing import List
from pprint import pprint


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i < j:
            m = (i+j) >> 1
            left, right, mid = nums[m-1], nums[m+1], nums[m]
            if left < mid > right:
                return m
            elif mid > right:
                j = m
            else:
                i = m+1
        return i


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 1, 3, 5, 6, 4]
        expected = 5
        self.assertEqual(sol.findPeakElement(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 2, 3, 1]
        expected = 2
        self.assertEqual(sol.findPeakElement(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1, 2, 3, 5]
        expected = 3
        self.assertEqual(sol.findPeakElement(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [3, 2, 1, 0]
        expected = 0
        self.assertEqual(sol.findPeakElement(nums), expected)

    def test_case_5(self):
        sol = Solution()
        nums = [1, 2]
        expected = 1
        self.assertEqual(sol.findPeakElement(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
