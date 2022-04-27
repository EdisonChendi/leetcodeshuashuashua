import unittest
from typing import List
from pprint import pprint


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for intv in intervals[1:]:
            if intv[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intv[1])
            else:
                res.append(intv)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
