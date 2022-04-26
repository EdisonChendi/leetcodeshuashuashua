import unittest
from typing import List
from pprint import pprint

import collections
import math


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        ans = math.inf
        seen = collections.defaultdict(list)
        N = len(points)
        for i in range(N):
            xi, yi = points[i]
            for j in range(i+1, N):
                xj, yj = points[j]
                lij = (xi-xj)**2 + (yi-yj)**2
                xm, ym = (xi+xj)/2, (yi+yj)/2
                for xk, yk in seen[(xm, ym, lij)]:
                    l1 = math.sqrt((xk-xi)**2+(yk-yi)**2)
                    l2 = math.sqrt((xk-xj)**2+(yk-yj)**2)
                    area = l1*l2
                    ans = min(ans, area)
                seen[(xm, ym, lij)].append((xi, yi))
        return ans if ans < math.inf else 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
