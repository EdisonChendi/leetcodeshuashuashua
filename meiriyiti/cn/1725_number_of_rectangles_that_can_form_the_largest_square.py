import unittest
from typing import List
from pprint import pprint


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_ = 0
        res = 0
        for a, b in rectangles:
            l = min(a, b)
            if l == max_:
                res += 1
            elif l > max_:
                max_ = l
                res = 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
        expected = 3
        self.assertEqual(sol.countGoodRectangles(rectangles), expected)

    def test_case_2(self):
        sol = Solution()
        rectangles = [[2, 3], [3, 7], [4, 3], [3, 7]]
        expected = 3
        self.assertEqual(sol.countGoodRectangles(rectangles), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
