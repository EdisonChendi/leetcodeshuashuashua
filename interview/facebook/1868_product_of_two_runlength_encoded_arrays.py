import unittest
from typing import List
from pprint import pprint


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        def merge(res, cur):
            if res and res[-1][0] == cur[0]:
                res[-1][1] += cur[1]
            else:
                res.append(cur)

        res = []
        i = j = 0
        while i < len(encoded1) and j < len(encoded2):
            v1, f1 = encoded1[i]
            v2, f2 = encoded2[j]
            f = min(f1, f2)
            merge(res, [v1*v2, f])
            encoded1[i][1] -= f
            encoded2[j][1] -= f
            i += encoded1[i][1] == 0
            j += encoded2[j][1] == 0
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        encoded1 = [[1, 3], [2, 3]]
        encoded2 = [[6, 3], [3, 3]]
        expected = [[6, 6]]
        self.assertCountEqual(sol.findRLEArray(encoded1, encoded2), expected)

    def test_case_2(self):
        sol = Solution()
        encoded1 = [[1, 3], [2, 1], [3, 2]]
        encoded2 = [[2, 3], [3, 3]]
        expected = [[2, 3], [6, 1], [9, 2]]
        self.assertCountEqual(sol.findRLEArray(encoded1, encoded2), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
