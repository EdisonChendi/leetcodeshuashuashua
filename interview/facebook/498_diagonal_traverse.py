from gc import collect
import unittest
from typing import List
from pprint import pprint

import collections


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagnals = collections.defaultdict(list)
        H, W = len(mat), len(mat[0])
        for i, row in enumerate(mat):
            for j, n in enumerate(row):
                diagnals[i+j].append(n)
        res = []
        for i in range(H+W-1):
            if i % 2 == 0:
                res.extend(reversed(diagnals[i]))
            else:
                res.extend(diagnals[i])
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        exepcted = [1, 2, 4, 7, 5, 3, 6, 8, 9]
        self.assertListEqual(sol.findDiagonalOrder(mat), exepcted)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
