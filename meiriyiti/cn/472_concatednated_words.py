import unittest
from typing import List
from pprint import pprint
import collections


class TrieNode:

    def __init__(self) -> None:
        self.end_of_word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end_of_word

    def dfs(self, word: str, idx: int) -> bool:
        if idx == len(word):
            return True

        node = self.root
        for i in range(idx, len(word)):
            ch = word[i]
            if ch not in node.children:
                return False

            node = node.children[ch]
            if node.end_of_word and self.dfs(word, i+1):
                return True

        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []

        words.sort(key=len)
        trie = Trie()

        for w in words:
            if not w:
                continue
            if trie.dfs(w, 0):
                res.append(w)
            else:
                trie.insert(w)

        return res


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []

        words.sort(key=len)
        trie = Trie()

        for w in words:
            if not w:
                continue
            if trie.dfs(w, 0):
                res.append(w)
            else:
                trie.insert(w)

        return res


class TestTrieSolution(unittest.TestCase):

    def test_case_1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))


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
