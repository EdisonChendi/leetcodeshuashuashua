import unittest
from typing import List
from pprint import pprint
import re


class Solution:
    def countValidWords(self, sentence: str) -> int:

        # rexp = r"^(([a-z]+-[a-z]+)|([a-z]+))?[.,!]?$"
        rexp = r"^([a-z]+(-[a-z]+)?)?[.,!]?$"
        r = re.compile(rexp)

        return sum(bool(r.match(w)) for w in sentence.split())


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        sentence = "cat and  dog"
        expected = 3
        self.assertEqual(sol.countValidWords(sentence), expected)

    def test_case_2(self):
        sol = Solution()
        sentence = "!this  1-s b8d!"
        expected = 0
        self.assertEqual(sol.countValidWords(sentence), expected)

    def test_case_3(self):
        sol = Solution()
        sentence = "alice and  bob are playing stone-game10"
        expected = 5
        self.assertEqual(sol.countValidWords(sentence), expected)

    def test_case_4(self):
        sol = Solution()
        sentence = "cat and  d-o-g"
        expected = 2
        self.assertEqual(sol.countValidWords(sentence), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
