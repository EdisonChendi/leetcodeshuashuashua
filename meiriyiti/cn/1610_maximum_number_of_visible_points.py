import unittest
from typing import List
from pprint import pprint
import math
import bisect

def cal_angle(p1, p2):
    return math.atan2(p2[1]-p1[1], p2[0]-p1[0])

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        res = 0
        same_cnt = 0
        polars = []
        for p in points:
            if p == location:
                same_cnt += 1
            else:
                polars.append(cal_angle(location, p))
        polars.sort()
        polars += [a+2*math.pi for a in polars]
        angle = angle*math.pi/180
        for i,a in enumerate(polars):
            idx = bisect.bisect_right(polars, a+angle)
            res = max(res, idx-i)
        return same_cnt + res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        points = [[2,1],[2,2],[3,3]]; angle = 90; location = [1,1]
        expected = 3
        self.assertEqual(sol.visiblePoints(points, angle, location), expected)

    def test_case_2(self):
        sol = Solution()
        points = [[2,1],[2,2],[3,4],[1,1]]; angle = 90; location = [1,1]
        expected = 4
        self.assertEqual(sol.visiblePoints(points, angle, location), expected)

    def test_case_3(self):
        sol = Solution()
        points = [[1,0],[2,1]]; angle = 13; location = [1,1]
        expected = 1
        self.assertEqual(sol.visiblePoints(points, angle, location), expected)

    def test_case_4(self):
        sol = Solution()
        points = [[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]]
        angle = 0; location = [1,1]
        expected = 4
        self.assertEqual(sol.visiblePoints(points, angle, location), expected)

    def test_case_5(self):
        sol = Solution()
        points = [[0,0],[0,2]]
        angle = 90; location = [1,1]
        expected = 2
        self.assertEqual(sol.visiblePoints(points, angle, location), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
