from curses import pair_content
import unittest
from typing import List
from pprint import pprint

import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(nums, l, r):
            idx = random.randint(l, r)
            nums[r], nums[idx] = nums[idx], nums[r]
            j = l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[j], nums[r] = nums[r], nums[j]
            return j

        K = len(nums)-k
        l, r = 0, len(nums)-1
        p = partition(nums, l, r)
        while p != K:
            if p > K:
                r = p-1
            else:
                l = p+1
            p = partition(nums, l, r)
        return nums[p]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        expected = 5
        self.assertEqual(sol.findKthLargest(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        expected = 4
        self.assertEqual(sol.findKthLargest(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
