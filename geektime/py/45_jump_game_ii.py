import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def jump1(self, nums: List[int]) -> int:
        N = len(nums)
        counts = [math.inf, ]*(N-1) + [0, ]
        for i in reversed(range(N-1)):
            counts[i] = 1+min(counts[idx]
                              for idx in range(i, min(i+nums[i], N-1)+1))
        return counts[0]

    def jump(self, nums: List[int]) -> int:
        count, m, end = 0, 0, 0
        for i in range(len(nums)-1):
            m = max(i + nums[i], m)
            if i == end:
                count += 1
                end = m
        return count


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 1, 1, 4]
        expected = 2
        self.assertEqual(sol.jump(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [2, 3, 0, 1, 4]
        expected = 2
        self.assertEqual(sol.jump(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [2, 3]
        expected = 1
        self.assertEqual(sol.jump(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [2]
        expected = 0
        self.assertEqual(sol.jump(nums), expected)

    def test_case_5(self):
        sol = Solution()
        nums = [1, 1, 1, 1, 100]
        expected = 4
        self.assertEqual(sol.jump(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
