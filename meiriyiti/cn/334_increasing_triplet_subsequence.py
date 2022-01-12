import unittest
from typing import List
from pprint import pprint

import math


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return False

        first, second = nums[0], math.inf
        for n in nums[1:]:
            if n > second:
                return True
            if n > first:
                second = n
            else:
                first = n
        return False


class TestSolution(unittest.TestCase):

    def test_case_0(self):
        sol = Solution()
        nums = [5, 1, 6]
        expected = False
        self.assertEqual(sol.increasingTriplet(nums), expected)

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5]
        expected = True
        self.assertEqual(sol.increasingTriplet(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [5, 4, 3, 2, 1]
        expected = False
        self.assertEqual(sol.increasingTriplet(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [2, 1, 5, 0, 4, 6]
        expected = True
        self.assertEqual(sol.increasingTriplet(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [4, 5, 2147483647, 1, 2]
        expected = True
        self.assertEqual(sol.increasingTriplet(nums), expected)

    def test_case_5(self):
        sol = Solution()
        nums = [1, 2, 2147483647]
        expected = True
        self.assertEqual(sol.increasingTriplet(nums), expected)

    def test_case_6(self):
        sol = Solution()
        nums = [0, 4, 2, 1, 0, -1, -3]
        expected = False
        self.assertEqual(sol.increasingTriplet(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
