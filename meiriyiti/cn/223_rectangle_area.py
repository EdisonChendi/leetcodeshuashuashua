import unittest
from typing import List
from pprint import pprint


def square(x1, y1, x2, y2):
    return (x2-x1)*(y2-y1)


def intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if any((by2 <= ay1, ay2 <= by1, ax2 <= bx1, bx2 <= ax1)):
        return 0

    return (min(ay2, by2)-max(ay1, by1)) * (min(ax2, bx2)-max(ax1, bx1))


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        return square(ax1, ay1, ax2, ay2) + square(bx1, by1, bx2, by2) - intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        expected = 45
        self.assertEqual(sol.computeArea(ax1=-3, ay1=0, ax2=3,
                         ay2=4, bx1=0, by1=-1, bx2=9, by2=2), expected)

    def test_case_2(self):
        sol = Solution()
        expected = 16
        self.assertEqual(sol.computeArea(ax1=-2, ay1=-2, ax2=2,
                         ay2=2, bx1=-2, by1=-2, bx2=2, by2=2), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
