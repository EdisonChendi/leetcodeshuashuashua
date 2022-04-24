import unittest
from typing import List
from pprint import pprint

import collections


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for n in nums:
            nxt_dp = collections.defaultdict(int)
            for i, cnt in dp.items():
                nxt_dp[i+n] += cnt
                nxt_dp[i-n] += cnt
            dp = nxt_dp
        return dp[target]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 1, 1, 1, 1]
        target = 3
        expected = 5
        self.assertEqual(sol.findTargetSumWays(nums, target), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1]
        target = 1
        expected = 1
        self.assertEqual(sol.findTargetSumWays(nums, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
