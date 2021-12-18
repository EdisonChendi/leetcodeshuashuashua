import unittest
from typing import List
from pprint import pprint


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_no_circle(nums: List[int]) -> int:
            y, n = 0, 0
            for m in nums:
                y, n = n+m, max(y, n)
            return max(y, n)

        if len(nums) <= 2:
            return max(nums)

        # 3 cases:
        # 1.consider 1st, but not last
        # 2.consider last, but not 1st
        # 3.consider neither 1st nor last
        # but case 3 is redundunt
        # return max(rob_no_circle(nums[:-1]), rob_no_circle(nums[1:]), rob_no_circle(nums[1:-1]))
        return max(rob_no_circle(nums[:-1]), rob_no_circle(nums[1:]))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 2]
        expected = 3
        self.assertEqual(sol.rob(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 2, 3, 1]
        expected = 4
        self.assertEqual(sol.rob(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1, 2, 3]
        expected = 3
        self.assertEqual(sol.rob(nums), expected)

    def test_edge_case_1(self):
        sol = Solution()
        nums = [1]
        expected = 1
        self.assertEqual(sol.rob(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
