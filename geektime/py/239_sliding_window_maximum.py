import unittest
from typing import List
from pprint import pprint
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums), ]

        res = []
        window = deque()
        for i in range(len(nums)):
            if window and window[0] == i-k:
                window.popleft()
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertListEqual(sol.maxSlidingWindow(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1]
        k = 1
        expected = [1]
        self.assertListEqual(sol.maxSlidingWindow(nums, k), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1, -1]
        k = 1
        expected = [1, -1]
        self.assertListEqual(sol.maxSlidingWindow(nums, k), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [9, 11]
        k = 2
        expected = [11]
        self.assertListEqual(sol.maxSlidingWindow(nums, k), expected)

    def test_case_5(self):
        sol = Solution()
        nums = [4, -2]
        k = 2
        expected = [4]
        self.assertListEqual(sol.maxSlidingWindow(nums, k), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
