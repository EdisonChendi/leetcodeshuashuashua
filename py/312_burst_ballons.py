import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxCoins1(self, nums: List[int]) -> int:
        # top-down
        nums = [1]+nums+[1]
        cache = {}

        def dp(l, r):
            if r-l == 1:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            res = max((nums[i]*nums[l]*nums[r]+dp(l, i)+dp(i, r))
                      for i in range(l+1, r))
            cache[(l, r)] = res
            return res

        return dp(0, len(nums)-1)

    def maxCoins(self, nums: List[int]) -> int:
        # bottom-up dp
        nums = [1]+nums+[1]
        N = len(nums)
        dp = [[0, ]*N for _ in range(N)]
        for g in range(2, N):
            for i in range(N-g):
                dp[i][i+g] = max((
                    nums[i]*nums[k]*nums[i+g] + dp[i][k]+dp[k][i+g]
                ) for k in range(i+1, i+g))

        return dp[0][-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3, 1, 5, 8]
        expected = 167
        self.assertEqual(sol.maxCoins(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 5]
        expected = 10
        self.assertEqual(sol.maxCoins(nums), expected)

    def test_edge_case_1(self):
        sol = Solution()
        nums = [5]
        expected = 5
        self.assertEqual(sol.maxCoins(nums), expected)


if __name__ == "__main__":
    unittest.main()
