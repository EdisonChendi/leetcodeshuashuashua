import unittest
from typing import List
from pprint import pprint


class Solution1:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # cool DP solution - but LTE
        ans = 0
        dp = [0]*(k+1)
        for i, n in enumerate(nums):
            new_dp = dp[:]
            for j in range(min(k, i+1)+1):
                if n == 1:
                    new_dp[j] = dp[j]+1
                else:
                    new_dp[j] = (dp[j-1]+1) if j > 0 else 0
                ans = max(ans, new_dp[j])
            dp = new_dp
        return ans


class Solution2:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # smart solution - sliding window
        # k consecutive, a window which holds at most k zeros
        N = len(nums)
        res = 0
        lsum = rsum = 0
        left = 0
        for right in range(N):
            n = nums[right]
            rsum += 1-n
            while rsum-lsum > k:
                lsum += 1-nums[left]
                left += 1
            res = max(res, right-left+1)
        return res


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # smartest solution - no inner loop
        N = len(nums)
        res = 0
        left = 0
        for right in range(N):
            k -= 1-nums[right]
            if k < 0:
                k += 1-nums[left]
                left += 1
            res = max(res, right-left+1)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        expected = 6
        self.assertEqual(sol.longestOnes(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3
        expected = 10
        self.assertEqual(sol.longestOnes(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
