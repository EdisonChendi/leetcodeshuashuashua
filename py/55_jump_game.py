import unittest
from typing import List
from pprint import pprint


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = len(nums)-1
        for i in reversed(range(reach)):
            if i+nums[i] >= reach:
                reach = i
        return reach == 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 1, 1, 4]
        expected = True
        self.assertEqual(sol.canJump(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3, 2, 1, 0, 4]
        expected = False
        self.assertEqual(sol.canJump(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
