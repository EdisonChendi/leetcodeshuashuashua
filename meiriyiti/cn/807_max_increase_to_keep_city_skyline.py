import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]

        return sum(min(row_max[i], col_max[j])-n
                   for i, row in enumerate(grid)
                   for j, n in enumerate(row))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
        expected = 35
        self.assertEqual(sol.maxIncreaseKeepingSkyline(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = 0
        self.assertEqual(sol.maxIncreaseKeepingSkyline(grid), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
