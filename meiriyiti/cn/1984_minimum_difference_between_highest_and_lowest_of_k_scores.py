import unittest
from typing import List
from pprint import pprint


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        return min(a-b for a, b in zip(nums[k-1:], nums))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [9, 4, 1, 7]
        k = 2
        expected = 2
        self.assertEqual(sol.minimumDifference(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [90]
        k = 1
        expected = 0
        self.assertEqual(sol.minimumDifference(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
