from msilib.schema import RadioButton
import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def cut(ribbons, l):
            return sum(r//l for r in ribbons)

        lo, hi = 1, max(ribbons)
        while lo <= hi:
            mid = (lo+hi) >> 1
            cnt = cut(ribbons, mid)
            if cnt >= k:
                lo = mid+1
            else:
                hi = mid-1
        return hi


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
