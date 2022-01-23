import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        L = len(nums1)
        s, n = 1, 0
        vs, vn = (nums2[0], nums1[0]), (nums1[0], nums2[0])
        for i in range(1, L):
            n1, n2 = nums1[i], nums2[i]
            # no swap:
            no_s = min(
                s if n1 > vs[0] and n2 > vs[1] else math.inf,
                n if n1 > vn[0] and n2 > vn[1] else math.inf
            )
            # swap:
            do_s = 1 + min(
                s if n2 > vs[0] and n1 > vs[1] else math.inf,
                n if n2 > vn[0] and n1 > vn[1] else math.inf
            )
            s, n = do_s, no_s
            vs, vn = (n2, n1), (n1, n2)
        return min(s, n)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums1 = [1, 3, 5, 4]
        nums2 = [1, 2, 3, 7]
        expected = 1
        self.assertEqual(sol.minSwap(nums1, nums2), expected)

    def test_case_2(self):
        sol = Solution()
        nums1 = [0, 3, 5, 8, 9]
        nums2 = [2, 1, 4, 6, 9]
        expected = 1
        self.assertEqual(sol.minSwap(nums1, nums2), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
