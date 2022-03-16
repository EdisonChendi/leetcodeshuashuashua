import unittest
from typing import List
from pprint import pprint

class Solution1:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            si, ei = firstList[i]
            sj ,ej = secondList[j]

            if si > ej:
                j += 1
            elif sj > ei:
                i += 1
            else: 
                res.append([max(si, sj), min(ei, ej)])
                if ej >= ei:
                    i += 1
                else:
                    j += 1
        return res

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            si, ei = firstList[i]
            sj ,ej = secondList[j]

            lo = max(si, sj)
            hi = min(ei, ej)

            if lo <= hi:
                res.append([lo, hi])
            
            if ej >= ei:
                i += 1
            else:
                j += 1 

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        firstList = [[0,2],[5,10],[13,23],[24,25]]
        secondList = [[1,5],[8,12],[15,24],[25,26]]
        expected = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        self.assertCountEqual(sol.intervalIntersection(firstList, secondList), expected)
        
    def test_case_2(self):
        sol = Solution()
        firstList = [[1,3],[5,9]]
        secondList = []
        expected = []
        self.assertCountEqual(sol.intervalIntersection(firstList, secondList), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
