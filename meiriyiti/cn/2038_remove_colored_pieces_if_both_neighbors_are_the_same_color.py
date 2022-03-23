import collections
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def winnerOfGame(self, colors: str) -> bool:
        cnt_A = cnt_B = 0
        ab = cnt = -1
        for ch in colors:
            if ch == 'A':
                if ab == 0:
                    cnt += 1
                else:
                    if ab == 1 and cnt > 2:
                        cnt_B += cnt - 2
                    ab = 0
                    cnt = 1
            else:
                if ab == 1:
                    cnt += 1
                else:
                    if ab == 0 and cnt > 2:
                        cnt_A += cnt - 2
                    ab = 1
                    cnt = 1
        else:
            if cnt > 2:
                if colors[-1] == 'A':
                    cnt_A += cnt-2
                else:
                    cnt_B += cnt-2
        return cnt_A > cnt_B


class Solution2:
    def winnerOfGame(self, colors: str) -> bool:
        A = B = 0
        for a, b, c in zip(colors, colors[1:], colors[2:]):
            if a == b == c:
                A += a == 'A'
                B += a == 'B'
        return A > B


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        counter = collections.Counter(a for a, b, c in zip(
            colors, colors[1:], colors[2:]) if a == b == c)
        return counter['A'] > counter['B']


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        colors = "AAABABB"
        expected = True
        self.assertEqual(sol.winnerOfGame(colors), expected)

    def test_case_2(self):
        sol = Solution()
        colors = "AA"
        expected = False
        self.assertEqual(sol.winnerOfGame(colors), expected)

    def test_case_3(self):
        sol = Solution()
        colors = "ABBBBBBBAAA"
        expected = False
        self.assertEqual(sol.winnerOfGame(colors), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
