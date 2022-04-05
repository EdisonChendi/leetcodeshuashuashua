import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        while l < r:
            hl, hr = height[l], height[r]
            res = max(res, (r-l)*min(hl, hr))
            if hl <= hr:
                l += 1
            else:
                r -= 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        self.assertEqual(sol.maxArea(height), expected)

    def test_case_2(self):
        sol = Solution()
        height = [1, 1]
        expected = 1
        self.assertEqual(sol.maxArea(height), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
