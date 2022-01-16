import unittest
from typing import List
from pprint import pprint


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        prev = 0
        res = 0
        for i in range(2, len(nums)):
            cur = 0
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                cur = 1 + prev
                res += cur
            prev = cur
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3, 4]
        expected = 3
        self.assertEqual(sol.numberOfArithmeticSlices(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1]
        expected = 0
        self.assertEqual(sol.numberOfArithmeticSlices(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5, 7, 8, 9]
        expected = 7
        self.assertEqual(sol.numberOfArithmeticSlices(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
