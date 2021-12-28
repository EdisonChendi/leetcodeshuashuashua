import unittest
from typing import List
from pprint import pprint


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        pass


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        words = ["cat", "cats", "catsdogcats", "dog",
                 "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
        expected = ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
        self.assertCountEqual(
            sol.findAllConcatenatedWordsInADict(words), expected)

    def test_case_2(self):
        sol = Solution()
        words = ["cat", "dog", "catdog"]
        expected = ["catdog"]
        self.assertCountEqual(
            sol.findAllConcatenatedWordsInADict(words), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
