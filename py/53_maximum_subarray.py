import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_, m = nums[0], nums[0]
        for i in range(1, len(nums)):
            m = max(nums[i], m+nums[i])
            max_ = max(max_, m)
        return max_


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        self.assertEqual(sol.maxSubArray(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1]
        expected = 1
        self.assertEqual(sol.maxSubArray(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [5, 4, -1, 7, 8]
        expected = 23
        self.assertEqual(sol.maxSubArray(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
