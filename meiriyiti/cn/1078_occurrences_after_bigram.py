import unittest
from typing import List
from pprint import pprint


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        n = len(words)
        return [words[k] for i, j, k in zip(range(n),
                                            range(1, n),
                                            range(2, n))
                if words[i] == first and words[j] == second]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        text = "alice is a good a good girl she is a good student"
        first = "a"
        second = "good"
        expected = ["a", "girl", "student"]
        self.assertListEqual(sol.findOcurrences(text, first, second), expected)

    def test_case_2(self):
        sol = Solution()
        text = "we will we will rock you"
        first = "we"
        second = "will"
        expected = ["we", "rock"]
        self.assertListEqual(sol.findOcurrences(text, first, second), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
