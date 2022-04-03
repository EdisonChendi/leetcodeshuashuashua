from bisect import bisect_right
import unittest
from typing import List
from pprint import pprint

import bisect


class Solution1:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N == 1:
            return

        m_ = nums[-1]
        arr = [nums[-1]]
        i = N-2
        while i >= 0:
            n = nums[i]
            if n < m_:
                break
            arr.append(n)
            m_ = n
            i -= 1
        else:
            nums.sort()
            return

        arr.sort()
        idx = bisect.bisect_right(arr, nums[i])
        nums[i], arr[idx] = arr[idx], nums[i]
        nums[i+1:] = arr


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N = len(nums)
        i = N-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = N-1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        l = i+1
        r = N-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l = l+1
            r = r-1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3]
        expected = [1, 3, 2]
        sol.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3, 2, 1]
        expected = [1, 2, 3]
        sol.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1, 1, 5]
        expected = [1, 5, 1]
        sol.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_case_4(self):
        sol = Solution()
        nums = [2, 4, 1, 2, 10]
        expected = [2, 4, 1, 10, 2]
        sol.nextPermutation(nums)
        self.assertEqual(nums, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
