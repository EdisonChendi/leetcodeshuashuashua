import unittest
from typing import List
from pprint import pprint

MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split("-"))
        return sum((sum(MONTH[:m]), d, (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) and m > 2))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        date = "2019-01-09"
        expected = 9
        self.assertEqual(sol.dayOfYear(date), expected)

    def test_case_2(self):
        sol = Solution()
        date = "2019-02-10"
        expected = 41
        self.assertEqual(sol.dayOfYear(date), expected)

    def test_case_3(self):
        sol = Solution()
        date = "2003-03-01"
        expected = 60
        self.assertEqual(sol.dayOfYear(date), expected)

    def test_case_4(self):
        sol = Solution()
        date = "2004-03-01"
        expected = 61
        self.assertEqual(sol.dayOfYear(date), expected)

    def test_case_5(self):
        sol = Solution()
        date = "2012-01-02"
        expected = 2
        self.assertEqual(sol.dayOfYear(date), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
