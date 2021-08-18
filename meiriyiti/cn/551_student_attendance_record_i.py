import unittest
from typing import List
from pprint import pprint


class Solution:
    def checkRecord(self, s: str) -> bool:
        a, l = 0, 0
        for r in s:
            l = l*(r == 'L')+(r == 'L')
            a += (r == 'A')
            if l == 3 or a == 2:
                return False
        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "PPALLP"
        expected = True
        self.assertEqual(sol.checkRecord(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "PPALLL"
        expected = False
        self.assertEqual(sol.checkRecord(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "PPALLPLL"
        expected = True
        self.assertEqual(sol.checkRecord(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "LALL"
        expected = True
        self.assertEqual(sol.checkRecord(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
