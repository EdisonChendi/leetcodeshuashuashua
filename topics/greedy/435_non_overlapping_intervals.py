import unittest
from typing import List
from pprint import pprint

import operator


class Solution1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # best approch - O(nlgn)
        # greedy - sort by end point
        remove = 0
        intervals.sort(key=operator.itemgetter(1))
        r = intervals[0][1]
        for i in range(1, len(intervals)):
            si, ri = intervals[i]
            if si < r:
                remove += 1
            else:
                r = ri
        return remove


class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(nlgn)
        # greedy - sort by start point
        remove = 0
        intervals.sort()
        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] >= prev[1]:
                prev = cur
            elif cur[1] < prev[1]:
                remove += 1
                prev = cur
            else:
                remove += 1
        return remove


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # by dp
        # dp[i] - end with intervals[i], the max number of non-overlapping intervals
        N = len(intervals)
        dp = [1]*N
        intervals.sort()
        for i in range(1, N):
            cur = intervals[i]
            dp[i] = max((dp[j] for j in range(i) if intervals[j][1] <= cur[0]),
                        default=0) + 1
        return N - max(dp)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        expected = 1
        self.assertEqual(sol.eraseOverlapIntervals(intervals), expected)

    def test_case_2(self):
        sol = Solution()
        intervals = [[1, 2], [1, 2], [1, 2]]
        expected = 2
        self.assertEqual(sol.eraseOverlapIntervals(intervals), expected)

    def test_case_3(self):
        sol = Solution()
        intervals = [[1, 2], [2, 3]]
        expected = 0
        self.assertEqual(sol.eraseOverlapIntervals(intervals), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
