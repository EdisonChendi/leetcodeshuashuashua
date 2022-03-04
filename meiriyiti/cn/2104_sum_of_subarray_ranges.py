import unittest
from typing import List
from pprint import pprint
import math

class Solution1:
    def subArrayRanges(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            max_val, min_val = -math.inf, math.inf
            for j in range(i, N):
                n = nums[j]
                max_val = max(max_val, n)
                min_val = min(min_val, n)
                ans += max_val - min_val
        return ans

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # ans = sum(range max - range min)
        #     = sum(range max) - sum(range min)
        #     = sum(nums[i]*max_cnt_i for all idx i) - sum(nums[i]*min_cnt_i for all idx i)
        # ===> Monostack
        N = len(nums)
        min_stack = []; min_left = [-1]*N
        max_stack = []; max_left = [-1]*N
        for i, n in enumerate(nums):
            while min_stack and nums[min_stack[-1]] > n:
                min_stack.pop()
            min_left[i] = min_stack[-1] if min_stack else -1
            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] <= n:
                max_stack.pop()
            max_left[i] = max_stack[-1] if max_stack else -1
            max_stack.append(i)
        
        min_stack = []; min_right = [-1]*N
        max_stack = []; max_right = [-1]*N
        for i in reversed(range(N)):
            n = nums[i]
            while min_stack and nums[min_stack[-1]] >= n:
                min_stack.pop()
            min_right[i] = min_stack[-1] if min_stack else N
            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] < n:
                max_stack.pop()
            max_right[i] = max_stack[-1] if max_stack else N
            max_stack.append(i)

        sum_max, sum_min = 0, 0
        for i in range(N):
            n = nums[i]
            sum_max += (i-max_left[i])*(max_right[i]-i)*n
            sum_min += (i-min_left[i])*(min_right[i]-i)*n
        return sum_max - sum_min

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,2,3]
        expected = 4
        self.assertEqual(sol.subArrayRanges(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1,3,3]
        expected = 4
        self.assertEqual(sol.subArrayRanges(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [4,-2,-3,4,1]
        expected = 59
        self.assertEqual(sol.subArrayRanges(nums), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
