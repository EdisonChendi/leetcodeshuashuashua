import unittest
from typing import List
from pprint import pprint
import heapq
import random


class Solution:
    def smallestK1(self, arr: List[int], k: int) -> List[int]:
        # time complexity: O(nlgk)
        # space complexity: O(k)
        k_nums = []
        for i in range(k):
            heapq.heappush(k_nums, -arr[i])
        for i in range(k, len(arr)):
            heapq.heappushpop(k_nums, -arr[i])
        return [-n for n in k_nums]

    def smallestK(self, arr: List[int], k: int) -> List[int]:
        def pivot(arr, l, r):
            p = arr[r]
            j = l-1
            for i in range(l, r):
                if arr[i] <= p:
                    j += 1
                    arr[j], arr[i] = arr[i], arr[j]
            arr[j+1], arr[r] = arr[r], arr[j+1]
            return j+1

        def helper(arr, l, r, k):
            pivot_idx = random.randint(l, r)
            arr[r], arr[pivot_idx] = arr[pivot_idx], arr[r]
            pos = pivot(arr, l, r)
            num = pos - l + 1
            if num > k:
                helper(arr, l, pos-1, k)
            elif num < k:
                helper(arr, pos+1, r, k-num)

        if k == 0 or not arr:
            return []
        helper(arr, 0, len(arr)-1, k)
        return arr[:k]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [1, 3, 5, 7, 2, 4, 6, 8]
        k = 4
        expected = [1, 2, 3, 4]
        self.assertCountEqual(sol.smallestK(arr, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
