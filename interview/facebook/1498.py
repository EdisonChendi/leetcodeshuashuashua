from bisect import bisect
import unittest
from typing import List
from pprint import pprint

import bisect


class Solution1:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9+7
        nums.sort()
        res = 0
        N = len(nums)
        for i, n in enumerate(nums):
            comp = target - n
            if comp < n:
                break
            idx = bisect.bisect_right(nums, comp, lo=i+1)
            res = (res + pow(2, idx-i-1, MOD)) % MOD
        return res % MOD


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9+7
        nums.sort()
        res = 0
        l, r = 0, len(nums)-1
        while l <= r:
            nl, nr = nums[l], nums[r]
            if nl + nr > target:
                r -= 1
            else:
                res = (res + pow(2, r-l, MOD)) % MOD
                l += 1
        return res % MOD


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3, 5, 6, 7]
        target = 9
        expected = 4
        self.assertEqual(sol.numSubseq(nums, target), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3, 3, 6, 8]
        target = 10
        expected = 6
        self.assertEqual(sol.numSubseq(nums, target), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [2, 3, 3, 4, 6, 7]
        target = 12
        expected = 61
        self.assertEqual(sol.numSubseq(nums, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
