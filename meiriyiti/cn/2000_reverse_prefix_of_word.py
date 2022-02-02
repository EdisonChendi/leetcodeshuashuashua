import unittest
from typing import List
from pprint import pprint


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c == ch:
                return word[:i+1][::-1]+word[i+1:]
        return word


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        word = "abcdefd"
        ch = "d"
        expected = "dcbaefd"
        self.assertEqual(sol.reversePrefix(word, ch), expected)

    def test_case_2(self):
        sol = Solution()
        word = "abcd"
        ch = "z"
        expected = "abcd"
        self.assertEqual(sol.reversePrefix(word, ch), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
