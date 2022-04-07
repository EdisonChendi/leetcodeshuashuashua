import unittest
from typing import List
from pprint import pprint


class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        last, end = 0, -1
        i = 0
        while i < N:
            if nums[i] == 0:
                if i > 0 and nums[i-1] == 1:
                    res = max(res, last+1)
                i += 1
            else:
                start = i
                while i < N and nums[i] == 1:
                    i += 1
                cur = i-start
                if start - end == 1:
                    if end >= 0:
                        res = max(res, cur+last+1)
                    else:
                        res = cur
                elif start > 0:
                    res = max(res, cur+1)
                last, end = cur, i
        return max(res, 1)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        dp0 = dp1 = 0
        for n in nums:
            if n == 1:
                dp0 += 1
                dp1 += 1
            else:
                dp1 = dp0 + 1
                dp0 = 0
            ans = max(ans, dp0, dp1)
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 0, 1, 1, 0]
        expected = 4
        self.assertEqual(sol.findMaxConsecutiveOnes(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 0, 1, 1, 0, 1]
        expected = 4
        self.assertEqual(sol.findMaxConsecutiveOnes(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1, 0, 1, 1, 0, 1, 1]
        expected = 5
        self.assertEqual(sol.findMaxConsecutiveOnes(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [1, 1, 0, 1, 1, 1, 0]
        expected = 6
        self.assertEqual(sol.findMaxConsecutiveOnes(nums), expected)

    def test_case_5(self):
        sol = Solution()
        nums = [1, 1, 1, 1, 0]
        expected = 5
        self.assertEqual(sol.findMaxConsecutiveOnes(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
