import unittest
from typing import List
from pprint import pprint
import collections


class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end_of_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        n = self._startsWith(word)
        return n != None and n.end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._startsWith(prefix) != None

    def _startsWith(self, prefix: str) -> TrieNode:
        node = self.root
        for ch in prefix:
            # Python trick: defaultdict, [] may creaet a new key, get won't
            # node = node.children.get(ch)
            if ch in node.children:
                node = node.children[ch]
            else:
                return None
        return node


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(trie.search("apple"), True)
        self.assertEqual(trie.search("app"), False)
        self.assertEqual(trie.startsWith("app"), True)
        trie.insert("app")
        self.assertEqual(trie.search("app"), True)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
