import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N

        dp = [(1, 1), ]
        res = collections.defaultdict(int)
        res[1] = 1
        for i in range(1, N):
            n, max_length, max_count = nums[i], 1, 1
            for j in range(i):
                if n <= nums[j]:
                    continue
                inc = dp[j][0]+1
                if max_length <= inc:
                    max_count = dp[j][1] + max_count*(max_length == inc)
                    max_length = inc
            dp.append((max_length, max_count))
            res[max_length] += max_count

        return max(res.items())[1]


class TestSolution(unittest.TestCase):

    # def test_case_1(self):
    #     sol = Solution()
    #     nums = [1, 3, 5, 4, 7]
    #     expected = 2
    #     self.assertEqual(sol.findNumberOfLIS(nums), expected)

    # def test_case_2(self):
    #     sol = Solution()
    #     nums = [2, 2, 2, 2, 2]
    #     expected = 5
    #     self.assertEqual(sol.findNumberOfLIS(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()
    #     nums = [2]
    #     expected = 1
    #     self.assertEqual(sol.findNumberOfLIS(nums), expected)

    # def test_edge_case_2(self):
    #     sol = Solution()
    #     nums = [1, 2]
    #     expected = 1
    #     self.assertEqual(sol.findNumberOfLIS(nums), expected)

    # def test_case_3(self):
    #     sol = Solution()
    #     nums = [1, 2, 4, 3, 5, 4, 7, 2]
    #     expected = 3
    #     self.assertEqual(sol.findNumberOfLIS(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        expected = 10
        self.assertEqual(sol.findNumberOfLIS(nums), expected)


if __name__ == "__main__":
    unittest.main()
