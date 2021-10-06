import unittest
from typing import List
from pprint import pprint
import heapq
import math


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a, b, c = -math.inf, -math.inf, -math.inf
        for n in nums:
            if n > a:
                a, b, c = n, a, b
            elif a > n > b:
                a, b, c = a, n, b
            elif b > n > c:
                a, b, c = a, b, n
        return c if c != -math.inf else a

    def thirdMax2(self, nums: List[int]) -> int:
        seen, h = set(), []
        for n in nums:
            if n not in seen:
                seen.add(n)
                if len(h) < 3:
                    heapq.heappush(h, n)
                else:
                    heapq.heappushpop(h, n)
        if len(h) < 3:
            return max(h)
        else:
            return h[0]

    def thirdMax1(self, nums: List[int]) -> int:
        nums = [-n for n in set(nums)]
        heapq.heapify(nums)
        if len(nums) < 3:
            return -heapq.heappop(nums)
        heapq.heappop(nums)
        heapq.heappop(nums)
        return -heapq.heappop(nums)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3, 2, 1]
        expected = 1
        self.assertEqual(sol.thirdMax(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 2]
        expected = 2
        self.assertEqual(sol.thirdMax(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [2, 2, 3, 1]
        expected = 1
        self.assertEqual(sol.thirdMax(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [1, 1, 2]
        expected = 2
        self.assertEqual(sol.thirdMax(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
