import math
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def maxRotateFunction(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        for i in range(N):
            cur = 0
            for j in range(N):
                cur += j*nums[(i+j) % N]
            res = max(res, cur)
        return res


class Solution2:
    def maxRotateFunction(self, nums: List[int]) -> int:
        L = len(nums)
        nums = nums + nums
        pre_sums = [0]
        for n in nums:
            pre_sums.append(pre_sums[-1]+n)
        res = cur = sum(k*nums[k] for k in range(L))
        for i in range(L, len(nums)):
            cur = cur + (L-1)*nums[i] - (pre_sums[i]-pre_sums[i-L+1])
            res = max(res, cur)
        return res


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)
        N = len(nums)
        cur = res = sum(i*n for i, n in enumerate(nums))
        for i in range(1, len(nums)):
            cur = cur + s - N * nums[N-i]
            res = max(res, cur)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [4, 3, 2, 6]
        expected = 26
        self.assertEqual(sol.maxRotateFunction(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [100]
        expected = 0
        self.assertEqual(sol.maxRotateFunction(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
