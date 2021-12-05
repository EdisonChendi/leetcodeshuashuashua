import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n0 = nums[0]
        ma, mi, ma_sum, mi_sum, total = n0, n0, n0, n0, n0
        for i in range(1, len(nums)):
            n = nums[i]
            ma_sum = max(ma_sum+n, n)
            ma = max(ma, ma_sum)
            mi_sum = min(mi_sum+n, n)
            mi = min(mi, mi_sum)
            total += n
        return max(ma, total-mi) if ma >= 0 else ma


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, -2, 3, -2]
        expected = 3
        self.assertEqual(sol.maxSubarraySumCircular(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [5, -3, 5]
        expected = 10
        self.assertEqual(sol.maxSubarraySumCircular(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [3, -1, 2, -1]
        expected = 4
        self.assertEqual(sol.maxSubarraySumCircular(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [3, -2, 2, -3]
        expected = 3
        self.assertEqual(sol.maxSubarraySumCircular(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [-2, -3, -1]
        expected = -1
        self.assertEqual(sol.maxSubarraySumCircular(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
