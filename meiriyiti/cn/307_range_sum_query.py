import unittest
from typing import List
from pprint import pprint

from math import log, ceil


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0]*(2**(ceil(log(len(nums))/log(2))+1))
        for i, n in enumerate(nums):
            self.update(i, n)

    def update(self, i: int, val: int) -> None:
        def helper(idx, l, r):
            if l == r:
                self.tree[idx] = val
                return
            mid = (l+r) >> 1
            if i <= mid:
                helper(2*idx+1, l, mid)
            else:
                helper(2*idx+2, mid+1, r)
            self.tree[idx] = self.tree[2*idx+1]+self.tree[2*idx+2]

        helper(0, 0, len(self.nums)-1)

    def sumRange(self, i: int, j: int) -> int:
        def helper(idx, l, r):
            if i > r or j < l:
                return 0

            if i <= l <= r <= j:
                return self.tree[idx]

            mid = (l+r) >> 1
            return helper(2*idx+1, l, mid) + helper(2*idx+2, mid+1, r)

        return helper(0, 0, len(self.nums)-1)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        numArray = NumArray([1, 3, 5])
        self.assertEqual(numArray.sumRange(0, 2), 9)  # return 1 + 3 + 5 = 9
        numArray.update(1, 2)  # nums = [1, 2, 5]
        self.assertEqual(numArray.sumRange(0, 2), 8)  # return 1 + 2 + 5 = 8

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
