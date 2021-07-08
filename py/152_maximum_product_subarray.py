import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = -math.inf
        pos, neg = 0, 0
        for n in nums:
            if n >= 0:
                pos, neg = max(pos*n, n), neg * n
            else:
                pos, neg = neg * n, min(pos*n, n)
            res = max(res, pos)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, -2, 4]
        res = 6
        self.assertEqual(sol.maxProduct(nums), res)

    def test_case_2(self):
        sol = Solution()
        nums = [-2, 0, -1]
        res = 0
        self.assertEqual(sol.maxProduct(nums), res)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
