import unittest
from typing import List
from pprint import pprint

import bisect


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        d = []
        while n > 0:
            n, r = divmod(n, 10)
            d.append(r)

        L = len(d)
        for i in range(L-1):
            if d[i+1] >= d[i]:
                continue
            idx = bisect.bisect_right(d, d[i+1], lo=0, hi=i+1)
            d[i+1], d[idx] = d[idx], d[i+1]
            d[:i+1] = d[:i+1][::-1]
            res = sum([d[n]*(10**n) for n in range(L)])
            return res if res < 1 << 31 else -1
        return -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 12
        expected = 21
        self.assertEqual(sol.nextGreaterElement(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 21
        expected = -1
        self.assertEqual(sol.nextGreaterElement(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 123456
        expected = 123465
        self.assertEqual(sol.nextGreaterElement(n), expected)

    def test_case_4(self):
        sol = Solution()
        n = 612345
        expected = 612354
        self.assertEqual(sol.nextGreaterElement(n), expected)

    def test_case_5(self):
        sol = Solution()
        n = 652345
        expected = 652354
        self.assertEqual(sol.nextGreaterElement(n), expected)

    def test_case_6(self):
        sol = Solution()
        n = 7812
        expected = 7821
        self.assertEqual(sol.nextGreaterElement(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
