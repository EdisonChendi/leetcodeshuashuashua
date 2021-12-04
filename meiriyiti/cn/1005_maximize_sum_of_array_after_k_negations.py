import unittest
from typing import List
from pprint import pprint


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k > 0 and i < len(nums) and nums[i] < 0:
            nums[i] *= -1
            i += 1
            k -= 1

        if k == 0:
            return sum(nums)

        # k > 0
        if i == len(nums):
            if k & 1 == 1:
                return sum(nums) - 2*nums[-1]
            else:
                return sum(nums)
        else:
            # nums[i] >= 0
            if k & 1 == 1:
                return sum(nums) - 2*min(nums[i], nums[i-1])
            else:
                return sum(nums)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [4, 2, 3]
        k = 1
        expected = 5
        self.assertEqual(sol.largestSumAfterKNegations(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3, -1, 0, 2]
        k = 3
        expected = 6
        self.assertEqual(sol.largestSumAfterKNegations(nums, k), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [2, -3, -1, 5, -4]
        k = 2
        expected = 13
        self.assertEqual(sol.largestSumAfterKNegations(nums, k), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [-1]
        k = 0
        expected = -1
        self.assertEqual(sol.largestSumAfterKNegations(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
