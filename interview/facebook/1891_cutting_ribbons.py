import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if k > sum(ribbons):
            return 0
        l = 1
        r = max(ribbons)+1

        def feasible(cut):
            cnt = 0
            for r in ribbons:
                cnt += r // cut
                if cnt >= k:
                    return True
            return False

        while l < r:
            m = (l+r+1) >> 1
            if feasible(m):
                l = m
            else:
                r = m-1
        return l


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        ribbons = [9, 7, 5]
        k = 3
        expected = 5
        self.assertEqual(sol.maxLength(ribbons, k), expected)

    def test_case_2(self):
        sol = Solution()
        ribbons = [7, 5, 9]
        k = 4
        expected = 4
        self.assertEqual(sol.maxLength(ribbons, k), expected)

    def test_case_3(self):
        sol = Solution()
        ribbons = [5, 7, 9]
        k = 22
        expected = 0
        self.assertEqual(sol.maxLength(ribbons, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
