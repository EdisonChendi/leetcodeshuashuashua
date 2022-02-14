import unittest
from typing import List
from pprint import pprint


class Solution1:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def helper(i: int, j: int) -> int:
            if i == j:
                return nums[i]

            m = (i+j) >> 1
            mid, left, right = nums[m], nums[m-1], nums[m+1]
            if left != mid != right:
                return mid

            if (j-i)//2 % 2 == 1:
                lo, hi = (m+1, j) if left == mid else (i, m-1)
            else:
                lo, hi = (i, m-2) if left == mid else (m+2, j)

            return helper(lo, hi)

        return helper(0, len(nums)-1)


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            m = (lo+hi) >> 1
            if m % 2 == 0:
                if nums[m] == nums[m+1]:
                    lo = m+2
                else:
                    hi = m
            else:
                if nums[m-1] == nums[m]:
                    lo = m+1
                else:
                    hi = m
        return nums[lo]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        expected = 2
        self.assertEqual(sol.singleNonDuplicate(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3, 3, 7, 7, 10, 11, 11]
        expected = 10
        self.assertEqual(sol.singleNonDuplicate(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [3, 3, 7]
        expected = 7
        self.assertEqual(sol.singleNonDuplicate(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [2, 2, 3, 5, 5]
        expected = 3
        self.assertEqual(sol.singleNonDuplicate(nums), expected)

    def test_case_5(self):
        sol = Solution()
        nums = [1]
        expected = 1
        self.assertEqual(sol.singleNonDuplicate(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
