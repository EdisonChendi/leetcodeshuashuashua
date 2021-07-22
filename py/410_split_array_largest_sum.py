import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # dp[i][j] - 截止到i，分j组，的最小分(最大和)分组
        # transfer func:
        # dp[i][j] = min(min(dp[i-k][j-1], sum(k,j)) for k in range())
        N = len(nums)
        dp = [[0, ]*(m+1) for _ in range(N+1)]
        pre_sum = [0, ]
        for i, n in enumerate(nums):
            pre_sum.append(pre_sum[-1]+n)

        for i in range(1, N+1):
            dp[i][1] = pre_sum[i]-pre_sum[0]
            for j in range(2, min(m, i)+1):
                dp[i][j] = min((max(dp[i-k][j-1], pre_sum[i]-pre_sum[i-k])
                                for k in range(1, i+1) if i-k >= j-1))
        return dp[-1][-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [7, 2, 5, 10, 8]
        m = 2
        expected = 18
        self.assertEqual(sol.splitArray(nums, m), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5]
        m = 2
        expected = 9
        self.assertEqual(sol.splitArray(nums, m), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1, 4, 4]
        m = 3
        expected = 4
        self.assertEqual(sol.splitArray(nums, m), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
