import unittest
from typing import List
from pprint import pprint

'''
* 线性dp问题
* dp[i]只依赖dp[i-1]
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = -10**4-1
        res = dp
        for n in nums:
            dp = max(n+dp, n)
            res = max(res, dp)
        return res


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
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
