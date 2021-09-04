import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height)-1
        while i < j:
            hi, hj = height[i], height[j]
            cur = min(hi, hj)*(j-i)
            res = max(res, cur)
            if hi < hj:
                i += 1
            else:
                j -= 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        height = [1, 1]
        expected = 1
        self.assertEqual(sol.maxArea(height), expected)

    def test_case_2(self):
        sol = Solution()
        height = [4, 3, 2, 1, 4]
        expected = 16
        self.assertEqual(sol.maxArea(height), expected)

    def test_case_3(self):
        sol = Solution()
        height = [1, 2, 1]
        expected = 2
        self.assertEqual(sol.maxArea(height), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
