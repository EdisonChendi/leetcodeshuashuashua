import bisect
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i <= j:
            mid = (i+j) >> 1
            m = nums[mid]
            if m == target:
                return mid
            elif m > target:
                j = mid-1
            else:
                i = mid+1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        return idx if idx < len(nums) and nums[idx] == target else -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        expected = 4
        self.assertEqual(sol.search(nums, target), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        expected = -1
        self.assertEqual(sol.search(nums, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
