import unittest
from typing import List
from pprint import pprint
# from .binary_indexed_tree import BinaryIndexTree
from bisect import bisect_left


# aka. Wenwick Tree
class BinaryIndexTree:

    def __init__(self, arr):
        self._origial_arr = arr
        self.arr = [0, ]*(len(self._origial_arr)+1)
        for i, v in enumerate(self._origial_arr):
            self.inc(i+1, v)

    @staticmethod
    def lowbit(n):
        return n & (-n)

    def inc(self, i, v):
        self._origial_arr[i-1] = v
        while i < len(self.arr):
            self.arr[i] += v
            i += BinaryIndexTree.lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.arr[i]
            i -= BinaryIndexTree.lowbit(i)
        return res

    def query_range(self, i, j):
        return self.query(j) - self.query(i-1)


class Solution_1:
    # by Binary Indexed Tree
    def reversePairs(self, nums: List[int]) -> int:
        # shrink the range of nums
        nums_sorted = sorted(nums)
        N = len(nums)
        arr = [(bisect_left(nums_sorted, nums[i])+1) for i in range(N)]

        # reversed pair
        res = 0
        bit = BinaryIndexTree([0]*N)
        # for v in arr:
        #     res += bit.query_range(v+1, N)
        #     bit.inc(v, 1)
        for i in reversed(range(N)):
            v = arr[i]
            res += bit.query(v-1)
            bit.inc(v, 1)
        return res


class Solution:
    # by merge sort - counting reversed pairs
    def reversePairs(self, nums: List[int]) -> int:
        res = 0

        def merge_sort(nums, l, r):
            nonlocal res
            if r-l <= 1:
                return

            mid = (l+r) // 2

            merge_sort(nums, l, mid)
            merge_sort(nums, mid, r)

            i, j = l, mid
            arr = []
            while i < mid and j < r:
                ni, nj = nums[i], nums[j]
                if ni > nj:
                    arr.append(nj)
                    res += mid-i
                    j += 1
                else:
                    arr.append(ni)
                    i += 1
            else:
                if i == mid:
                    arr.extend(nums[j:r])
                else:
                    arr.extend(nums[i:mid])
            nums[l:r] = arr

        merge_sort(nums, 0, len(nums))
        return res


class TestSolution(unittest.TestCase):

    def test_case__1(self):
        sol = Solution()
        nums = [7, 5, 6, 4]
        expected = 5
        self.assertEqual(sol.reversePairs(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
