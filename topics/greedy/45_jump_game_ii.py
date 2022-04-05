import unittest
from typing import List
from pprint import pprint

import math


class Solution1:
    def jump(self, nums: List[int]) -> int:
        # dp
        N = len(nums)
        dp = [math.inf]*(N-1)+[0]
        for i in reversed(range(N-1)):
            dp[i] = 1 + min([dp[j] for j in range(i+1, min(i+nums[i]+1, N))],
                            default=math.inf)
        return dp[0]


class Solution2:
    def jump(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        longest = 0
        for i in range(len(nums)-1):
            n = nums[i]
            longest = max(longest, i+n)
            if i == cur:
                res += 1
                cur = longest
        return res


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        longest = 0
        for i in range(len(nums)-1):
            n = nums[i]
            longest = max(longest, i+n)
            if i == cur:
                cur = longest
                res += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 1, 1, 4]
        expected = 2
        self.assertEqual(sol.jump(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [2, 3, 0, 1, 4]
        expected = 2
        self.assertEqual(sol.jump(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [0]
        expected = 0
        self.assertEqual(sol.jump(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [1, 1, 1, 1]
        expected = 3
        self.assertEqual(sol.jump(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
