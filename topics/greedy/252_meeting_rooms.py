import unittest
from typing import List
from pprint import pprint

import math


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        end = -math.inf
        for s, e in intervals:
            if s < end:
                return False
            end = max(end, e)
        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        intervals = [[0, 30], [5, 10], [15, 20]]
        expected = False
        self.assertEqual(sol.canAttendMeetings(intervals), expected)

    def test_case_2(self):
        sol = Solution()
        intervals = [[7, 10], [2, 4]]
        expected = True
        self.assertEqual(sol.canAttendMeetings(intervals), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
