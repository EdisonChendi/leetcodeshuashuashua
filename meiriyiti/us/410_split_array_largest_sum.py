import math
import unittest
from typing import List
from pprint import pprint


class Solution1:
    # binary search
    # O(Nlog(Sum))
    def splitArray(self, nums: List[int], m: int) -> int:
        def can_split(mid: int, nums: List[int], m: int) -> bool:
            accu = 0
            cnt = 0
            for n in nums:
                if n > mid:
                    return False
                if accu + n <= mid:
                    accu += n
                else:
                    cnt += 1
                    accu = n
            cnt += 1
            return cnt <= m

        l = min(nums)
        r = sum(nums)
        while l < r:
            mid = (l+r) >> 1
            if can_split(mid, nums, m):
                r = mid
            else:
                l = mid + 1
        return l


class Solution:
    # DP
    # dp[i][j] - up until ith number | split into j subarrays
    # dp[i][j] = min(dp[k][j-1] + sum(k+1, i) for k from j-1 to i-1)

    def splitArray(self, nums: List[int], m: int) -> int:
        pre_sums = [0]
        for n in nums:
            pre_sums.append(pre_sums[-1]+n)

        dp = [[None]*(m+1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][1] = pre_sums[i+1]
            for j in range(2, min(i+1, m)+1):
                dp[i][j] = min([max(dp[k][j-1], pre_sums[i+1]-pre_sums[k+1])
                               for k in range(j-2, i)])

        return dp[-1][-1]


class TestSolution(unittest.TestCase):

    def test_case_0(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5]
        m = 1
        expected = 15
        self.assertEqual(sol.splitArray(nums, m), expected)

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
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
