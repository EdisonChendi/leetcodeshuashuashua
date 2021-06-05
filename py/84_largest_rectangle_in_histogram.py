import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-math.inf, -1), ]
        res = -math.inf
        l = len(heights)
        for i, h in enumerate(heights):
            while stack and h < stack[-1][0]:
                top_h, _ = stack.pop()
                res = max(res, top_h*(i-stack[-1][1]-1))
            stack.append((h, i))
        while len(stack) > 1:
            h, _ = stack.pop()
            res = max(res, h*(l-1-stack[-1][1]))
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        heights = [2, 1, 5, 6, 2, 3]
        expected = 10
        self.assertEqual(sol.largestRectangleArea(heights), expected)

    def test_case_2(self):
        sol = Solution()
        heights = [2, 4]
        expected = 4
        self.assertEqual(sol.largestRectangleArea(heights), expected)

    def test_case_3(self):
        sol = Solution()
        heights = [5, 4, 1, 2]
        expected = 8
        self.assertEqual(sol.largestRectangleArea(heights), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
