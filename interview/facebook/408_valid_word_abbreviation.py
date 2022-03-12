import unittest
from typing import List
from pprint import pprint


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        la, lw = len(abbr), len(word)
        while i < la and j < lw:
            if abbr[i].isalpha():
                if abbr[i] != word[j]:
                    return False
                i, j = i+1, j+1
            else:
                if abbr[i] == '0':
                    return False
                cur = 0
                while i < la and abbr[i].isdigit():
                    cur = cur*10 + ord(abbr[i]) - ord('0')
                    i += 1
                j += cur
        return i == la and j == lw


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        word = "internationalization"
        abbr = "i12iz4n"
        expected = True
        self.assertEqual(sol.validWordAbbreviation(word, abbr), expected)

    def test_case_2(self):
        sol = Solution()
        word = "apple"
        abbr = "a2e"
        expected = False
        self.assertEqual(sol.validWordAbbreviation(word, abbr), expected)

    def test_case_3(self):
        sol = Solution()
        word = "substitution"
        abbr = "12"
        expected = True
        self.assertEqual(sol.validWordAbbreviation(word, abbr), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
