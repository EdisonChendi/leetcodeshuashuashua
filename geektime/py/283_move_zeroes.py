import unittest
from typing import List
from pprint import pprint


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # z - starting index of consecutive zeroes
        # p - pointer moving along the list
        z = p = 0
        while p < len(nums):
            if nums[p] != 0:
                nums[p], nums[z] = nums[z], nums[p]
                z += 1
            p += 1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        sol.moveZeroes(nums)
        self.assertListEqual(nums, expected)

    def test_case_2(self):
        sol = Solution()
        nums = [0]
        expected = [0]
        sol.moveZeroes(nums)
        self.assertListEqual(nums, expected)

    def test_normal_case_3(self):
        sol = Solution()
        nums = [2, 1]
        expected = [2, 1]
        sol.moveZeroes(nums)
        self.assertListEqual(nums, expected)

    def test_edge_case_1(self):
        sol = Solution()
        nums = [1, 0]
        expected = [1, 0]
        sol.moveZeroes(nums)
        self.assertListEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()
