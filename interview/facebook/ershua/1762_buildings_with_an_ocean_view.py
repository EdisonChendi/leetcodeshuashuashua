import unittest
from typing import List
from pprint import pprint


class Solution1:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(N)
        # mono stack
        res = []
        stack = []
        N = len(heights)
        for i in reversed(range(N)):
            h = heights[i]
            while stack and stack[-1] < h:
                stack.pop()
            if not stack:
                res.append(i)
            stack.append(h)
        return list(reversed(res))


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(1)
        res = []
        max_height = -1
        N = len(heights)
        for i in reversed(range(N)):
            h = heights[i]
            if h > max_height:
                max_height = h
                res.append(i)
        return list(reversed(res))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        heights = [4, 2, 3, 1]
        expected = [0, 2, 3]
        self.assertListEqual(sol.findBuildings(heights), expected)

    def test_case_2(self):
        sol = Solution()
        heights = [4, 3, 2, 1]
        expected = [0, 1, 2, 3]
        self.assertListEqual(sol.findBuildings(heights), expected)

    def test_case_3(self):
        sol = Solution()
        heights = [1, 3, 2, 4]
        expected = [3]
        self.assertListEqual(sol.findBuildings(heights), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
