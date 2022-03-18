import unittest
from typing import List
from pprint import pprint

class Solution1:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [-1]*N
        stack = []
        nums = nums+nums
        for i,n in enumerate(nums):
            while stack and stack[-1][1] < n:
                idx, _ = stack.pop()
                res[idx%N] = n
            stack.append((i,n))
        return res

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [-1]*N
        stack = []
        for _ in range(2):
            for i in range(N):
                while stack and nums[stack[-1]] < nums[i]:
                    res[stack.pop()] = nums[i]
                stack.append(i)
        return res

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,2,1]
        expected = [2,-1,2]
        self.assertListEqual(sol.nextGreaterElements(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1,2,3,4,3]
        expected = [2,3,4,-1,4]
        self.assertListEqual(sol.nextGreaterElements(nums), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
