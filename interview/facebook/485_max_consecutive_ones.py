import unittest
from typing import List
from pprint import pprint


class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        N = len(nums)
        while i < N:
            if nums[i] == 0:
                i += 1
                continue
            start = i
            while i < N and nums[i] == 1:
                i += 1
            ans = max(ans, i-start)
        return ans


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
            elif n == 0:
                count = 0
            ans = max(ans, count)
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 1, 0, 1, 1, 1]
        expected = 3
        self.assertEqual(sol.findMaxConsecutiveOnes(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 0, 1, 1, 0, 1]
        expected = 2
        self.assertEqual(sol.findMaxConsecutiveOnes(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
