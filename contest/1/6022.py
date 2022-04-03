import unittest
from typing import List
from pprint import pprint

import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = 0
        h = []
        for n in nums:
            total += n
            heapq.heappush(h, -n)

        target = total/2
        cnt = 0
        while total > target:
            n = -heapq.heappop(h)
            half = n/2
            total -= half
            heapq.heappush(h, -half)
            cnt += 1
        return cnt


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [5, 19, 8, 1]
        expected = 3
        self.assertEqual(sol.halveArray(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
