from secrets import randbelow
import unittest
from typing import List
from pprint import pprint

import random
import bisect


class Solution1:

    def __init__(self, w: List[int]):
        self.w = w
        self.pre_sum = [0]
        for n in w:
            self.pre_sum.append(self.pre_sum[-1]+n)

    def pickIndex(self) -> int:
        p = random.randint(0, self.pre_sum[-1]-1)
        return bisect.bisect_right(self.pre_sum, p)-1


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.pre_sum = [0]
        for n in w:
            self.pre_sum.append(self.pre_sum[-1]+n)

    def pickIndex(self) -> int:
        n = self.pre_sum[-1]*random.random()
        l, r = 0, len(self.pre_sum)
        while l < r:
            m = (l+r) >> 1
            mid = self.pre_sum[m]
            if mid == n:
                return m
            if n > mid:
                l = m + 1
            else:
                r = m
        return l-1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
