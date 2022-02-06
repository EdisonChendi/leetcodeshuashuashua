import unittest
from typing import List
from pprint import pprint


class Solution1:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        presums = [0]
        for n in nums:
            presums.append(presums[-1]+n)

        N = len(nums)
        dp = [[0, ]*(k+1) for _ in range(N)]
        for i, n in enumerate(nums):
            dp[i][0], dp[i][1] = 0, presums[i+1]/(i+1)
            for j in range(2, 1+min(k, i+1)):
                dp[i][j] = max(dp[ii][j-1] + (presums[i+1] -
                               presums[ii+1]) / (i-ii) for ii in range(j-2, i))
        return dp[-1][-1]


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # 同样的思路，简化solution1
        presums = [0]
        for n in nums:
            presums.append(presums[-1]+n)

        def average(i, j):
            return (presums[j]-presums[i]) / (j-i)

        N = len(nums)
        dp = [average(i, N) for i in range(N)]
        for _ in range(k-1):
            for i in range(N):
                for j in range(i+1, N):
                    dp[i] = max(dp[i], dp[j]+average(i, j))
        return dp[0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [9, 1, 2, 3, 9]
        k = 3
        expected = 20.0
        self.assertEqual(sol.largestSumOfAverages(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 4
        expected = 20.5000
        self.assertEqual(sol.largestSumOfAverages(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
