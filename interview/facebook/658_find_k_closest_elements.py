from collections import deque
import unittest
from typing import List
from pprint import pprint

import bisect
import collections


class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = collections.deque()
        i = bisect.bisect_left(arr, x) - 1
        j = i + 1
        while i >= 0 and j < len(arr) and k > 0:
            ni, nj = arr[i], arr[j]
            if abs(ni-x) <= abs(nj-x):
                res.appendleft(ni)
                i -= 1
            else:
                res.append(nj)
                j += 1
            k -= 1

        if k != 0:
            if i < 0:
                res.extend(arr[j:j+k])
            else:
                res.extendleft(reversed(arr[i+1-k:i+1]))
        return list(res)


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-k
        while left < right:
            mid = (left+right) >> 1
            if x-arr[mid] <= arr[mid+k]-x:
                right = mid
            else:
                left = mid+1
        return arr[left:left+k]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = 3
        expected = [1, 2, 3, 4]
        self.assertListEqual(sol.findClosestElements(arr, k, x), expected)

    def test_case_2(self):
        sol = Solution()
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = -1
        expected = [1, 2, 3, 4]
        self.assertListEqual(sol.findClosestElements(arr, k, x), expected)

    def test_case_3(self):
        sol = Solution()
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = 7
        expected = [2, 3, 4, 5]
        self.assertListEqual(sol.findClosestElements(arr, k, x), expected)

    def test_case_4(self):
        sol = Solution()
        arr = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
        k = 3
        x = 5
        expected = [3, 3, 4]
        self.assertListEqual(sol.findClosestElements(arr, k, x), expected)

# def test_edge_case_1(self):
#     sol = Solution()


if __name__ == "__main__":
    unittest.main()
