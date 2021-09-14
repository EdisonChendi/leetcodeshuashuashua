import unittest
from typing import List
from pprint import pprint


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def match(s, word):
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j = j+1
                i += 1
            return j == len(word)

        dictionary.sort(key=lambda w: (-len(w), w))
        for word in dictionary:
            if match(s, word):
                return word
        return ""


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "abpcplea"
        dictionary = ["ale", "apple", "monkey", "plea"]
        expected = "apple"
        self.assertEqual(sol.findLongestWord(s, dictionary), expected)

    def test_case_2(self):
        sol = Solution()
        s = "abpcplea"
        dictionary = ["a", "b", "c"]
        expected = "a"
        self.assertEqual(sol.findLongestWord(s, dictionary), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
