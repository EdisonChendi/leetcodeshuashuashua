import unittest
from typing import List
from pprint import pprint


class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        pos, neg, res = 0, 0, 0
        for n in nums:
            if n < 0:
                pos, neg = neg*n, min(n, pos*n)
            else:
                pos, neg = max(n, pos*n), n*neg
            res = max(res, pos)

        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma, mi, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            ma, mi = max(n, max(ma*n, mi*n)), min(n, min(ma*n, mi*n))
            res = max(res, ma)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, -2, 4]
        expected = 6
        self.assertEqual(sol.maxProduct(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [-2, 0, -1]
        expected = 0
        self.assertEqual(sol.maxProduct(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [-2]
        expected = -2
        self.assertEqual(sol.maxProduct(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [-4, -3, -2]
        expected = 12
        self.assertEqual(sol.maxProduct(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
