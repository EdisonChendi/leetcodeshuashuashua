import operator
import unittest
from typing import List
from pprint import pprint

import heapq


class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h = []
        res = 0
        for s, e in intervals:
            while h and s >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, e)
            res = max(res, len(h))
        return res


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0

        start = sorted(map(operator.itemgetter(0), intervals))
        end = sorted(map(operator.itemgetter(1), intervals))

        i = 0
        for s in start:
            if end[i] <= s:
                i += 1
            else:
                res += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        intervals = [[0, 30], [5, 10], [15, 20]]
        expected = 2
        self.assertEqual(sol.minMeetingRooms(intervals), expected)

    def test_case_2(self):
        sol = Solution()
        intervals = [[7, 10], [2, 4]]
        expected = 1
        self.assertEqual(sol.minMeetingRooms(intervals), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
