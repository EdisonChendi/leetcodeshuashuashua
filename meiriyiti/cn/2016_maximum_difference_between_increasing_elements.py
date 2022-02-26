import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        m = math.inf
        for n in nums:
            if n > m:
                res = max(res, n-m)
            m = min(m, n)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [7, 1, 5, 4]
        exepcted = 4
        self.assertEqual(sol.maximumDifference(nums), exepcted)

    def test_case_2(self):
        sol = Solution()
        nums = [9, 4, 3, 2]
        exepcted = -1
        self.assertEqual(sol.maximumDifference(nums), exepcted)

    def test_case_3(self):
        sol = Solution()
        nums = [1, 5, 2, 10]
        exepcted = 9
        self.assertEqual(sol.maximumDifference(nums), exepcted)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
