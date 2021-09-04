import unittest
from typing import List
from pprint import pprint


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for l in reversed(range(len(triangle)-1)):
            for i in range(len(triangle[l])):
                triangle[l][i] += min(triangle[l+1][i], triangle[l+1][i+1])
        return triangle[0][0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        expected = 11
        self.assertEqual(sol.minimumTotal(triangle), expected)

    def test_case_2(self):
        sol = Solution()
        triangle = [[-10]]
        expected = -10
        self.assertEqual(sol.minimumTotal(triangle), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
