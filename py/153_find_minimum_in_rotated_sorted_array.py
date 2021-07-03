import unittest
from typing import List
from pprint import pprint


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r) >> 1
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1
        return nums[l]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3, 4, 5, 1, 2]
        expected = 1
        self.assertEqual(sol.findMin(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [4, 5, 6, 7, 0, 1, 2]
        expected = 0
        self.assertEqual(sol.findMin(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [11, 13, 15, 17]
        expected = 11
        self.assertEqual(sol.findMin(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [5, 1, 2, 3, 4]
        expected = 1
        self.assertEqual(sol.findMin(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
