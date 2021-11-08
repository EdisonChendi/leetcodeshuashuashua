import unittest
from typing import List
from pprint import pprint
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        cows = sum((Counter(secret) & Counter(guess)).values())-bulls
        return f"{bulls}A{cows}B"

    def getHint1(self, secret: str, guess: str) -> str:
        bulls = 0
        scnt = [0]*10
        gcnt = [0]*10
        for s, g in zip(secret, guess):
            bulls += s == g
            scnt[int(s)] += 1
            gcnt[int(g)] += 1
        cows = sum(min(s, g) for s, g in zip(scnt, gcnt)) - bulls
        return f"{bulls}A{cows}B"


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        secret = "1807"
        guess = "7810"
        expected = "1A3B"
        self.assertEqual(sol.getHint(secret, guess), expected)

    def test_case_2(self):
        sol = Solution()
        secret = "1123"
        guess = "0111"
        expected = "1A1B"
        self.assertEqual(sol.getHint(secret, guess), expected)

    def test_case_3(self):
        sol = Solution()
        secret = "1"
        guess = "0"
        expected = "0A0B"
        self.assertEqual(sol.getHint(secret, guess), expected)

    def test_case_4(self):
        sol = Solution()
        secret = "1"
        guess = "1"
        expected = "1A0B"
        self.assertEqual(sol.getHint(secret, guess), expected)

# def test_edge_case_1(self):
#     sol = Solution()


if __name__ == "__main__":
    unittest.main()
