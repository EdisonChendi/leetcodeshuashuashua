import unittest
from typing import List
from pprint import pprint

import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = collections.Counter()
        banned = set(b.lower() for b in banned)
        word = []
        res_w = ""
        m = 0
        for ch in paragraph+" ":
            if ch in " !?',;.":
                w = "".join(word)
                if w and w not in banned:
                    counter[w] += 1
                    if counter[w] > m or counter[w] == m and w < res_w:
                        res_w = w
                        m = counter[w]
                word = []
            else:
                word.append(ch.lower())
        return res_w


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        paragraph = "a."
        banned = []
        expected = "a"
        self.assertEqual(sol.mostCommonWord(paragraph, banned), expected)

    def test_case_2(self):
        sol = Solution()
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        expected = "ball"
        self.assertEqual(sol.mostCommonWord(paragraph, banned), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
