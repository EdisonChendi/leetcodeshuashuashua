import unittest
from typing import List
from pprint import pprint


def to_min(t: str) -> int:
    h, m = t.split(":")
    return int(h)*60 + int(m)


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        diff = to_min(correct) - to_min(current)
        res = 0

        for span in (60, 15, 5, 1):
            c, diff = divmod(diff, span)
            res += c
            if diff == 0:
                break
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        current = "02:30"
        correct = "04:35"
        expected = 3
        self.assertEqual(sol.convertTime(current, correct), expected)

    def test_case_2(self):
        sol = Solution()
        current = "11:00"
        correct = "11:01"
        expected = 1
        self.assertEqual(sol.convertTime(current, correct), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
