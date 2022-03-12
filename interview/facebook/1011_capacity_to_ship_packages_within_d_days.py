import unittest
from typing import List
from pprint import pprint

import math
import bisect


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ma = -math.inf
        pre_sums = [0]
        for w in weights:
            ma = max(ma, w)
            pre_sums.append(pre_sums[-1]+w)

        N = len(weights)
        l, r = pre_sums[-1]//N, pre_sums[-1]

        def fit(cap):
            idx, accu = 0, 0
            for _ in range(days):
                accu += cap
                idx = bisect.bisect_right(pre_sums, accu, lo=idx)
                if idx == len(pre_sums):
                    return True
                accu = pre_sums[idx-1]
            return False

        while l < r:
            mid = (l+r) >> 1
            if fit(mid):
                r = mid
            else:
                l = mid+1
        return l


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        days = 5
        expected = 15
        self.assertEqual(sol.shipWithinDays(weights, days), expected)

    def test_case_2(self):
        sol = Solution()
        weights = [3, 2, 2, 4, 1, 4]
        days = 3
        expected = 6
        self.assertEqual(sol.shipWithinDays(weights, days), expected)

    def test_case_3(self):
        sol = Solution()
        weights = [1, 2, 3, 1, 1]
        days = 4
        expected = 3
        self.assertEqual(sol.shipWithinDays(weights, days), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
