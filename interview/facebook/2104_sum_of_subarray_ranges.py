import unittest
from typing import List
from pprint import pprint

import math


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def sumSubarrayMins(arr: List[int]) -> int:
            res = 0
            arr.append(-math.inf)
            stack = [-1]
            for i in range(len(arr)):
                while stack and arr[i] < arr[stack[-1]]:
                    idx = stack.pop()
                    res += arr[idx]*(i-idx)*(idx-stack[-1])
                stack.append(i)
            return res

        def sumSubarrayMaxs(arr: List[int]) -> int:
            res = 0
            arr.append(math.inf)
            stack = [-1]
            for i in range(len(arr)):
                while stack and arr[i] > arr[stack[-1]]:
                    idx = stack.pop()
                    res += arr[idx]*(i-idx)*(idx-stack[-1])
                stack.append(i)
            return res

        return sumSubarrayMaxs(nums[:]) - sumSubarrayMins(nums[:])


class TestSolution(unittest.TestCase):

    # def test_case_1(self):
    #     sol = Solution()
    #     nums = [1, 2, 3]
    #     expected = 4
    #     self.assertEqual(sol.subArrayRanges(nums), expected)

    # def test_case_2(self):
    #     sol = Solution()
    #     nums = [1, 3, 3]
    #     expected = 4
    #     self.assertEqual(sol.subArrayRanges(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [4, -2, -3, 4, 1]
        expected = 59
        self.assertEqual(sol.subArrayRanges(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
