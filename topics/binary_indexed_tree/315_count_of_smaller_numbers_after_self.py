from bisect import bisect_left
import unittest
from typing import List
from pprint import pprint


class BinaryIndexedTree:
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
            i += BinaryIndexedTree.lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.arr[i]
            i -= BinaryIndexedTree.lowbit(i)
        return res

    def query_range(self, i, j):
        return self.query(j) - self.query(i-1)


class Solution1:
    # solve by Binary Indexed Tree
    def countSmaller(self, nums: List[int]) -> List[int]:
        # shrink the range of nums
        N = len(nums)
        sorted_nums = sorted(nums)
        for i, n in enumerate(nums):
            nums[i] = bisect_left(sorted_nums, n)+1

        res = [0]*N
        # do the counting by Binary Indexed Tree
        bit = BinaryIndexedTree([0]*N)
        for i in reversed(range(N)):
            n = nums[i]
            res[i] = bit.query(n-1)
            bit.inc(n, 1)
        return res


class Solution:
    # solve by merge sort
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(arr, l, r, counter):
            if r-l <= 1:
                return

            mid = (l+r)//2
            merge_sort(arr, l, mid, counter)
            merge_sort(arr, mid, r, counter)

            i, j = l, mid
            temp = []
            while i < mid and j < r:
                ni, nj = arr[i], arr[j]
                if ni[1] <= nj[1]:
                    temp.append(ni)
                    i += 1
                    counter[ni[0]] += j-mid
                else:
                    temp.append(nj)
                    j += 1

            if i == mid:
                temp.extend(arr[j:r])
            else:
                while i < mid:
                    temp.append(arr[i])
                    counter[arr[i][0]] += j-mid
                    i += 1
            arr[l:r] = temp

        counter = [0]*len(nums)
        merge_sort(list(enumerate(nums)), 0, len(nums), counter)
        return counter


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [5, 2, 6, 1]
        expected = [2, 1, 1, 0]
        self.assertListEqual(sol.countSmaller(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [-1]
        expected = [0]
        self.assertListEqual(sol.countSmaller(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [-1, -1]
        expected = [0, 0]
        self.assertListEqual(sol.countSmaller(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
