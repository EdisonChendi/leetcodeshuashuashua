from time import time
import unittest
from typing import List
from pprint import pprint


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_minutes(time_point: str) -> int:
            h, m = time_point.split(":")
            return 60*int(h)+int(m)

        if len(timePoints) > 1440:
            return 0

        times = []
        for t in timePoints:
            mins = to_minutes(t)
            times.append(mins)
        times.sort()
        times.append(times[0]+24*60)
        return min(times[i]-times[i-1] for i in range(1, len(times)))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        timePoints = ["23:59", "00:00"]
        expected = 1
        self.assertEqual(sol.findMinDifference(timePoints), expected)

    def test_case_2(self):
        sol = Solution()
        timePoints = ["00:00", "23:59", "00:00"]
        expected = 0
        self.assertEqual(sol.findMinDifference(timePoints), expected)

    def test_case_3(self):
        sol = Solution()
        timePoints = ["00:00", "13:00"]
        expected = 660
        self.assertEqual(sol.findMinDifference(timePoints), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
