import unittest
from typing import List
from pprint import pprint


class Solution1:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = []
        for n in nums:
            cur = [n, ]
            for seq in dp:
                if n % seq[-1] == 0 and len(seq)+1 > len(cur):
                    cur = seq + [n, ]
            dp.append(cur)
        return max(dp, key=len)


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = []
        prev = []
        for i in range(len(nums)):
            n = nums[i]
            l, p = 1, -1
            for j in range(i):
                if n % nums[j] == 0 and dp[j]+1 > l:
                    l = dp[j]+1
                    p = j
            dp.append(l)
            prev.append(p)

        idx = -max((l, -i) for i, l in enumerate(dp))[1]
        res = []
        while idx != -1:
            res.append(nums[idx])
            idx = prev[idx]
        return list(reversed(res))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 4, 8]
        expected = [1, 2, 4, 8]
        self.assertListEqual(sol.largestDivisibleSubset(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 2, 3]
        expected = [1, 2]
        self.assertListEqual(sol.largestDivisibleSubset(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [2, 3, 5]
        expected = [2]
        self.assertListEqual(sol.largestDivisibleSubset(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
