import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        cache = {}

        def distance(i, j):
            p = (i, j) if i <= j else (j, i)
            if p in cache:
                return cache[p]
            p0, p1 = points[p[0]], points[p[1]]
            res = (p0[0]-p1[0])**2 + (p0[1]-p1[1])**2
            cache[p] = res
            return res

        res, N = 0, len(points)
        for i in range(N):
            dis = collections.defaultdict(int)
            for j in range(N):
                if i == j:
                    continue
                dis[distance(i, j)] += 1
            for m in dis.values():
                res += m*(m-1)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        points = [[0, 0], [1, 0], [2, 0]]
        expected = 2
        self.assertEqual(sol.numberOfBoomerangs(points), expected)

    def test_case_2(self):
        sol = Solution()
        points = [[1, 1], [2, 2], [3, 3]]
        expected = 2
        self.assertEqual(sol.numberOfBoomerangs(points), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
