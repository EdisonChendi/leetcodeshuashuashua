import unittest
from typing import List
from pprint import pprint
import collections


class TrieNode:

    def __init__(self):
        self.w = -1
        self.children = collections.defaultdict(TrieNode)


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word, idx):
        node = self.root
        for ch in word:
            node.w = idx
            node = node.children[ch]
        node.w = idx

    def prefix(self, pre):
        node = self.root
        for ch in pre:
            if ch in node.children:
                node = node.children[ch]
            else:
                return -1
        return node.w


class WordFilter:

    def __init__(self, words: List[str]):
        # N - number of words
        # L - length of the longest word
        # O(N*L^2)
        self.words = words
        self.trie = Trie()
        for i, w in enumerate(words):
            for j in reversed(range(len(w))):
                self.trie.add(w[j:]+'#'+w, i)

    def f(self, prefix: str, suffix: str) -> int:
        # O(L)
        return self.trie.prefix(suffix+'#'+prefix)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        words = ["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
                 "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"]
        obj = WordFilter(words)
        res = obj.f("bccbacbcba", "a")
        expected = 9
        self.assertEqual(res, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
