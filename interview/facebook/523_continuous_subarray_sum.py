import unittest
from typing import List
from pprint import pprint


class Solution1:
    # LTE
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        dp = [n % k for n in nums]
        for i in range(2, N+1):
            for j in range(N-i+1):
                rem = (dp[j]+nums[j+i-1]) % k
                if rem == 0:
                    return True
                dp[j] = rem
        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Key observation
        prev = {0: -1}
        rem = 0
        for i, n in enumerate(nums):
            rem = (rem + n) % k
            if rem in prev:
                if i-prev[rem] >= 2:
                    return True
            else:
                prev[rem] = i
        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [23, 2, 4, 6, 7]
        k = 6
        expected = True
        self.assertEqual(sol.checkSubarraySum(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [23, 2, 6, 4, 7]
        k = 6
        expected = True
        self.assertEqual(sol.checkSubarraySum(nums, k), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [23, 2, 6, 4, 7]
        k = 13
        expected = False
        self.assertEqual(sol.checkSubarraySum(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
