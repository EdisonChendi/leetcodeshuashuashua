import unittest
from typing import List
from pprint import pprint
import collections

class TrieNode:
    def __init__(self) -> None:
        self.children = collections.defaultdict(TrieNode)
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        return node

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        trie = Trie()
        nodes = [trie.add(w[::-1]) for w in words]
        return sum((1+len(words[i]) for i, n in enumerate(nodes) if len(n.children)== 0))

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        words = ["time", "me", "bell"]
        expected = 10
        self.assertEqual(sol.minimumLengthEncoding(words), expected)

    def test_case_2(self):
        sol = Solution()
        words = ["time", "time","time","time"]
        expected = 5
        self.assertEqual(sol.minimumLengthEncoding(words), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
