import unittest
from typing import List
from pprint import pprint
from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        count = 0 
        q = [beginWord]
        visited = set(q)
        while q:
            nxt_q = []
            count += 1
            for w in q:
                for i in range(len(w)):
                    for ch in ascii_lowercase:
                        wch = w[:i]+ch+w[i+1:] 
                        if wch not in visited and wch in wordList and wch != w:
                            if wch == endWord:
                                return count+1
                            visited.add(wch)
                            nxt_q.append(wch)
            q = nxt_q
        return 0



class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        expected = 5
        self.assertEqual(sol.ladderLength(beginWord, endWord, wordList), expected)

    def test_case_2(self):
        sol = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        expected = 0
        self.assertEqual(sol.ladderLength(beginWord, endWord, wordList), expected)

    def test_case_3(self):
        sol = Solution()
        beginWord = "hot"
        endWord = "dog"
        wordList = ["hot","dog"]
        expected = 0
        self.assertEqual(sol.ladderLength(beginWord, endWord, wordList), expected)

    def test_case_4(self):
        sol = Solution()
        beginWord = "hot"
        endWord = "hit"
        wordList = ["hit"]
        expected = 2
        self.assertEqual(sol.ladderLength(beginWord, endWord, wordList), expected)

        
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
