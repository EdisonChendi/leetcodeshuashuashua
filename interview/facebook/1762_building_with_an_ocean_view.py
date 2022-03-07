import unittest
from typing import List
from pprint import pprint

class Solution1:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        res = []
        for i in reversed(range(len(heights))):
            n = heights[i]
            while stack and stack[-1] < n:
                stack.pop()
            if not stack:
                res.append(i)
                stack.append(n)
        return list(reversed(res))

import math
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_ = -math.inf
        res = []
        for i in reversed(range(len(heights))):
            n = heights[i]
            if n > max_:
                max_ = n    
                res.append(i)
        return list(reversed(res))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        heights = [4,2,3,1]
        expected = [0,2,3]
        self.assertCountEqual(sol.findBuildings(heights), expected)

    def test_case_2(self):
        sol = Solution()
        heights = [4,3,2,1]
        expected = [0,1,2,3]
        self.assertCountEqual(sol.findBuildings(heights), expected)

    def test_case_3(self):
        sol = Solution()
        heights = [0,3,2,4]
        expected = [3]
        self.assertCountEqual(sol.findBuildings(heights), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
