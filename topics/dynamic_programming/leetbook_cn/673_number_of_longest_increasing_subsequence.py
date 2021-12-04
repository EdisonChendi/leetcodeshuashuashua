import unittest
from typing import List
from pprint import pprint


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [(1, 1), ]*N
        max_ = 1
        max_count = 1
        for i in range(1, N):
            n = nums[i]
            m_count = 1
            m = dp[i][0]
            for j in range(i):
                j_longest, j_count = dp[j]
                if n > nums[j]:
                    if j_longest+1 == m:
                        m_count += j_count
                    elif j_longest >= m:
                        m_count = j_count
                        m = j_longest+1
            dp[i] = (m, m_count)
            if m == max_:
                max_count += m_count
            elif m > max_:
                max_ = m
                max_count = m_count
        return max_count


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 3, 5, 4, 7]
        expected = 2
        self.assertEqual(sol.findNumberOfLIS(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 3, 5, 4, 7, 1, 3, 5, 4, 7]
        expected = 1
        self.assertEqual(sol.findNumberOfLIS(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [2, 2, 2, 2, 2]
        expected = 5
        self.assertEqual(sol.findNumberOfLIS(nums), expected)


if __name__ == "__main__":
    unittest.main()
