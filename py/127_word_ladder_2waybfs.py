import unittest
from typing import List
from pprint import pprint

import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # by 2-way BFS
        word_list = set(wordList)
        if endWord not in word_list:
            return 0

        dist, word_len = 0, len(beginWord)
        front, back = {beginWord}, {endWord}
        word_list -= {beginWord, endWord}
        while front:
            new_front = set()
            dist += 1
            for word in front:
                for i in range(word_len):
                    for ch in string.ascii_lowercase:
                        trans_word = word[:i] + ch + word[i+1:]
                        if trans_word in back:
                            return dist + 1
                        if trans_word in word_list:
                            word_list.discard(trans_word)
                            new_front.add(trans_word)
            front = new_front
            if len(front) < len(back):
                front, back = back, front
        return 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()

        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        expected = 5
        self.assertEqual(sol.ladderLength(
            beginWord, endWord, wordList), expected)

    def test_case_2(self):
        sol = Solution()

        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        expected = 0
        self.assertEqual(sol.ladderLength(
            beginWord, endWord, wordList), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
