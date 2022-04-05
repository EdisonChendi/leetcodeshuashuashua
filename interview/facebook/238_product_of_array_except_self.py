import unittest
from typing import List
from pprint import pprint


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = [1]+[0]*(N-1)
        right = [0]*(N-1)+[1]

        for i in range(1, N):
            if nums[i-1] == 0:
                break
            left[i] = left[i-1]*nums[i-1]

        for i in reversed(range(N-1)):
            if nums[i+1] == 0:
                break
            right[i] = right[i+1]*nums[i+1]

        res = [0]*N
        for i in range(N):
            res[i] = left[i]*right[i]
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1]*N
        for i in range(1, N):
            res[i] = res[i-1] * nums[i-1]

        R = 1
        for i in reversed(range(N-1)):
            R *= nums[i+1]
            res[i] *= R

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertListEqual(sol.productExceptSelf(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertListEqual(sol.productExceptSelf(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
