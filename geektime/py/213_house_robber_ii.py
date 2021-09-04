import unittest
from typing import List
from pprint import pprint


class Solution:
    def rob(self, nums: List[int]) -> int:
        def sub_rob(start, end, pre, now):
            for i in range(start, end+1):
                pre, now = now, max(pre+nums[i], now)
            return now

        y = sub_rob(1, len(nums)-2, 0, nums[0])
        n = sub_rob(1, len(nums)-1, 0, 0)
        return max(y, n)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 2]
        expected = 3
        self.assertEqual(sol.rob(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 2, 3, 1]
        expected = 4
        self.assertEqual(sol.rob(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [0]
        expected = 0
        self.assertEqual(sol.rob(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [5]
        expected = 5
        self.assertEqual(sol.rob(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
