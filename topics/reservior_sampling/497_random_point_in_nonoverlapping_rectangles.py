import bisect
import unittest
from typing import List
from pprint import pprint

import random


class Solution1:
    # WRONG

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

    def pick(self) -> List[int]:
        pick = -1
        for i in range(len(self.rects)):
            if random.randrange(i+1) == 0:
                pick = i
        ll_x, ll_y, tr_x, tr_y = self.rects[pick]
        return [random.randint(ll_x, tr_x), random.randint(ll_y, tr_y)]


class Solution2:
    # reservior sampling

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

    def pick(self) -> List[int]:
        total = 0
        pick = -1
        for rect in self.rects:
            ll_x, ll_y, tr_x, tr_y = rect
            s = (tr_x-ll_x+1)*(tr_y-ll_y+1)
            total += s
            if random.randrange(total) < s:
                pick = rect
        return [random.randint(pick[0], pick[2]), random.randint(pick[1], pick[3])]


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.pre = [0, ]
        for i in range(len(self.rects)):
            ll_x, ll_y, tr_x, tr_y = self.rects[i]
            area = (tr_x-ll_x+1)*(tr_y-ll_y+1)
            self.pre.append(self.pre[-1]+area)

    def pick(self) -> List[int]:
        p = random.randrange(self.pre[-1])
        idx = bisect.bisect_right(self.pre, p)-1
        ll_x, ll_y, tr_x, tr_y = self.rects[idx]
        return [random.randint(ll_x, tr_x), random.randint(ll_y, tr_y)]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
