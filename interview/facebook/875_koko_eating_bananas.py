import unittest
from typing import List
from pprint import pprint

import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k: int) -> bool:
            return sum(math.ceil(p/k) for p in piles) <= h

        l, r = 1, max(piles)
        while l < r:
            m = (l+r) >> 1
            if can_finish(m):
                r = m
            else:
                l = m+1
        return l


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        piles = [3, 6, 7, 11]
        h = 8
        expected = 4
        self.assertEqual(sol.minEatingSpeed(piles, h), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
