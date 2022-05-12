import unittest
from typing import List
from pprint import pprint


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        R = B = G = 0
        for r, b, g in costs:
            R, B, G = r + min(B, G), b + min(R, G), g + min(R, B)
        return min(R, B, G)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
        expected = 10
        self.assertEqual(sol.minCost(costs), expected)

    def test_case_2(self):
        sol = Solution()
        costs = [[7, 6, 2]]
        expected = 2
        self.assertEqual(sol.minCost(costs), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
