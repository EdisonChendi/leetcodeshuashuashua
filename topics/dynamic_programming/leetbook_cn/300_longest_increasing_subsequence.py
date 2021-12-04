import unittest
from typing import List
from pprint import pprint

'''
* 线性dp
* dp[i]所有之前的dp值
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res, N = 1, len(nums)
        dp = [1]*N
        for i in range(1, N):
            n = nums[i]
            for j in range(i):
                if n > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
            res = max(res, dp[i])
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        self.assertEqual(sol.lengthOfLIS(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [0, 1, 0, 3, 2, 3]
        expected = 4
        self.assertEqual(sol.lengthOfLIS(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [7, 7, 7, 7, 7, 7, 7]
        expected = 1
        self.assertEqual(sol.lengthOfLIS(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
