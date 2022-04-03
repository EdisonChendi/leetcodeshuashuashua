import unittest
from typing import List
from pprint import pprint


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # by simulation
        while len(nums) > 1:
            nxt_nums = []
            for i in range(len(nums)-1):
                nxt_nums.append((nums[i]+nums[i+1]) % 10)
            nums = nxt_nums
        return nums[0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5]
        expected = 8
        self.assertEqual(sol.triangularSum(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
