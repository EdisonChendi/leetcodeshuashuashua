import unittest
from typing import List
from pprint import pprint


class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        if N < 3:
            return 0

        l, r = 0, N-1
        lmax, rmax = height[l], height[r]
        res = 0
        while l < r:
            hl, hr = height[l], height[r]
            if hl < hr:
                if hl < lmax:
                    res += lmax - hl
                else:
                    lmax = hl
                l += 1
            else:
                if hr < rmax:
                    res += rmax - hr
                else:
                    rmax = hr
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
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
