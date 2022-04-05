import unittest
from typing import List
from pprint import pprint


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        l_max = r_max = 0
        while l < r:
            hl, hr = height[l], height[r]
            l_max = max(l_max, hl)
            r_max = max(r_max, hr)
            if hl < hr:
                res += l_max - hl
                l += 1
            else:
                res += r_max - hr
                r -= 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        self.assertEqual(sol.trap(height), expected)

    def test_case_2(self):
        sol = Solution()
        height = [4, 2, 0, 3, 2, 5]
        expected = 9
        self.assertEqual(sol.trap(height), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
