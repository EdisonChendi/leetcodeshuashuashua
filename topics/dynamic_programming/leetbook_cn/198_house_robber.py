import unittest
from typing import List
from pprint import pprint


class Solution:
    def rob(self, nums: List[int]) -> int:
        y, n = 0, 0
        for m in nums:
            y, n = n+m, max(y, n)
        return max(y, n)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3, 1]
        expected = 4
        self.assertEqual(sol.rob(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [2, 7, 9, 3, 1]
        expected = 12
        self.assertEqual(sol.rob(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
