import unittest
from typing import List
from pprint import pprint


import math


class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)

        def get(i):
            if i < 0 or i > N-1:
                return -math.inf
            else:
                return nums[i]

        for i in range(N):
            if get(i-1) < get(i) > get(i+1):
                return i
        return -1


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def get(i):
            return -math.inf if i < 0 or i > N-1 else nums[i]

        N = len(nums)
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) >> 1
            nl, nm, nr = get(m-1), get(m), get(m+1)
            if nl < nm > nr:
                return m
            if nm > nr:
                r = m-1
            else:
                l = m+1
        return -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
