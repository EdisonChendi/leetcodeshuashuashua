import unittest
from typing import List
from pprint import pprint

import math


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_make(size) -> bool:
            cnt = 0
            for c in candies:
                cnt += c // size
                if cnt >= k:
                    return True
            return False

        l = 0
        r = sum(candies)
        while l < r:
            mid = math.ceil((l+r)/2)
            can = can_make(mid)
            if can:
                l = mid
            else:
                r = mid - 1
        return l


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        candies = [5, 8, 6]
        k = 3
        expected = 5
        self.assertEqual(sol.maximumCandies(candies, k), expected)

    def test_case_2(self):
        sol = Solution()
        candies = [2, 5]
        k = 11
        expected = 0
        self.assertEqual(sol.maximumCandies(candies, k), expected)

    def test_case_3(self):
        sol = Solution()
        candies = [2, 5]
        k = 4
        expected = 1
        self.assertEqual(sol.maximumCandies(candies, k), expected)

    def test_case_4(self):
        sol = Solution()
        candies = [2, 5]
        k = 3
        expected = 2
        self.assertEqual(sol.maximumCandies(candies, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
