import unittest
from typing import List
from pprint import pprint

import heapq


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums

        N = len(nums)
        small = []  # max heap
        small_size = 0
        big = []  # min heap - Python built-in
        big_size = 0

        res = []
        for i in range(N):
            n = nums[i]

            heapq.heappush(small, (-n, -i))
            ns, s = heapq.heappop(small)

            heapq.heappush(big, (-ns, -s))
            big_size += 1

            l = i-k
            if l >= 0:
                nl = nums[l]
                if nl <= -small[0][0]:
                    small_size -= 1
                else:
                    big_size -= 1

            if small_size < big_size:
                nb, b = heapq.heappop(big)
                big_size -= 1
                heapq.heappush(small, (-nb, -b))
                small_size += 1

            while small and -small[0][1] <= l:
                heapq.heappop(small)

            while big and big[0][1] <= l:
                heapq.heappop(big)

            if small_size + big_size == k:
                if k % 2 == 1:
                    res.append(-small[0][0])
                else:
                    res.append((-small[0][0]+big[0][0])/2)

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
        self.assertListEqual(sol.medianSlidingWindow(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
        k = 3
        expected = [2.00000, 3.00000, 3.00000,
                    3.00000, 2.00000, 3.00000, 2.00000]
        self.assertListEqual(sol.medianSlidingWindow(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
