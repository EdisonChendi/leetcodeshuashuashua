import unittest
from typing import List
from pprint import pprint


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0, ]*(length+1)
        for s, e, inc in updates:
            res[s] += inc
            res[e+1] -= inc
        for i in range(length):
            res[i+1] += res[i]
        return res[:-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        length = 5
        updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
        expected = [-2, 0, 3, 5, 3]
        self.assertListEqual(sol.getModifiedArray(length, updates), expected)

    def test_case_2(self):
        sol = Solution()
        length = 10
        updates = [[2, 4, 6], [5, 6, 8], [1, 9, -4]]
        expected = [0, -4, 2, 2, 2, 4, 4, -4, -4, -4]
        self.assertListEqual(sol.getModifiedArray(length, updates), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
