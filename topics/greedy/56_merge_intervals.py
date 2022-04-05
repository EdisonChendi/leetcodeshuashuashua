import unittest
from typing import List
from pprint import pprint


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            si, ei = intervals[i]
            if si <= end:
                end = max(end, ei)
            else:
                res.append([start, end])
                start, end = si, ei
        res.append([start, end])
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertCountEqual(sol.merge(intervals), expected)

    def test_case_2(self):
        sol = Solution()
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertCountEqual(sol.merge(intervals), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
