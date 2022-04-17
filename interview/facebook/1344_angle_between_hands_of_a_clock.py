import unittest
from typing import List
from pprint import pprint


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        unit = 6
        min_angle = minutes * unit
        hour_angle = (hour % 12 + minutes/60)*5*unit
        btw = abs(min_angle-hour_angle)
        return min(btw, 360-btw)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        hour = 12
        minutes = 30
        expected = 165
        self.assertEqual(sol.angleClock(hour, minutes), expected)

    def test_case_2(self):
        sol = Solution()
        hour = 3
        minutes = 30
        expected = 75
        self.assertEqual(sol.angleClock(hour, minutes), expected)

    def test_case_3(self):
        sol = Solution()
        hour = 3
        minutes = 15
        expected = 7.5
        self.assertEqual(sol.angleClock(hour, minutes), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
