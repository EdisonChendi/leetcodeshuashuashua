import unittest
from typing import List
from pprint import pprint


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                # [0 - mid] increasing
                if nums[0] <= target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                # [mid - hi] increasing
                if nums[hi] >= target > nums[mid]:
                    lo = mid+1
                else:
                    hi = mid-1
        return -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        expected = 4
        self.assertEqual(sol.search(nums, target), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        expected = -1
        self.assertEqual(sol.search(nums, target), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1, ]
        target = 0
        expected = -1
        self.assertEqual(sol.search(nums, target), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [3, 1]
        target = 1
        expected = 1
        self.assertEqual(sol.search(nums, target), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
