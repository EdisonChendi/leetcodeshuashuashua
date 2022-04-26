import random
import unittest
from typing import List
from pprint import pprint

import heapq


class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(Nlgk)
        # Space: O(k)

        h = []

        def d(p):
            return p[0]**2+p[1]**2

        for i, p in enumerate(points):
            heapq.heappush(h, (-d(p), i))
            if len(h) > k:
                heapq.heappop(h)

        return [points[i] for _, i in h]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # quick select
        # Time: O(N)
        # Space: O(N)
        def quick_select(ps, k):
            l, r = 0, len(ps)-1
            pivot = partition(ps, l, r)
            while pivot+1 != k:
                if pivot+1 > k:
                    r = pivot
                else:
                    l = pivot+1
                pivot = partition(ps, l, r)
            return [points[ps[i][1]] for i in range(k)]

        def partition(ps, l, r):
            idx = random.randint(l, r)
            ps[idx], ps[r] = ps[r], ps[idx]

            j = l
            for i in range(l, r):
                if ps[i][0] <= ps[r][0]:
                    ps[j], ps[i] = ps[i], ps[j]
                    j += 1
            ps[j], ps[r] = ps[r], ps[j]
            return j

        def dist(p):
            return p[0]**2 + p[1]**2

        ps = [(dist(p), i) for i, p in enumerate(points)]

        return quick_select(ps, k)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        points = [[1, 3], [-2, 2]]
        k = 1
        expected = [[-2, 2]]
        self.assertCountEqual(sol.kClosest(points, k), expected)

    def test_case_2(self):
        sol = Solution()
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        expected = [[3, 3], [-2, 4]]
        self.assertCountEqual(sol.kClosest(points, k), expected)

    def test_case_3(self):
        sol = Solution()
        points = [[0, 1], [1, 0]]
        k = 2
        expected = [[0, 1], [1, 0]]
        self.assertCountEqual(sol.kClosest(points, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
