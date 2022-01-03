import unittest
from typing import List
from pprint import pprint


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        week = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]
        days = 4
        for y in range(1971, year):
            days += 365 + ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0)
        
        days += sum(months[:month-1]) + day + (month > 2 and ((year %
                                                               4 == 0 and year % 100 != 0) or year % 400 == 0))
        return week[days % 7]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        day = 31
        month = 8
        year = 2019
        expected = "Saturday"
        self.assertEqual(sol.dayOfTheWeek(day, month, year), expected)

    def test_case_2(self):
        sol = Solution()
        day = 18
        month = 7
        year = 1999
        expected = "Sunday"
        self.assertEqual(sol.dayOfTheWeek(day, month, year), expected)

    def test_case_3(self):
        sol = Solution()
        day = 15
        month = 8
        year = 1993
        expected = "Sunday"
        self.assertEqual(sol.dayOfTheWeek(day, month, year), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
