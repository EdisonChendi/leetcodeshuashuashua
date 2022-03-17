import collections
from random import randrange
import unittest
from typing import List
from pprint import pprint

import string


class Solution1:
    def longestWord(self, words: List[str]) -> str:
        ordered_words = [set() for _ in range(31)]
        for w in words:
            ordered_words[len(w)].add(w)

        prv = ordered_words[1]
        if not prv:
            return ""

        for i in range(2, 31):

            if not ordered_words[i]:
                return min(prv)
            else:
                nxt = set(
                    w+ch for w in prv for ch in string.ascii_letters if w+ch in ordered_words[i])
                if not nxt:
                    return min(prv)
                prv = nxt
        return min(prv)


class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.is_word = False


ORD_A = ord('a')


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            v = ord(ch) - ORD_A
            if not node.children[v]:
                node.children[v] = TrieNode()
            node = node.children[v]
        node.is_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            v = ord(ch) - ORD_A
            if not node.children[v] or not node.children[v].is_word:
                return False
            node = node.children[v]
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        for w in words:
            t.insert(w)

        ans = ""
        for w in words:
            if t.search(w) and (len(w) > len(ans) or len(w) == len(ans) and w < ans):
                ans = w
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        words = ["w", "wo", "wor", "worl", "world"]
        world = "world"
        self.assertEqual(sol.longestWord(words), world)

    def test_case_2(self):
        sol = Solution()
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        world = "apple"
        self.assertEqual(sol.longestWord(words), world)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
