import unittest
from typing import List
from pprint import pprint

import collections


class TrieNode:

    def __init__(self) -> None:
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        self.word = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True
        node.word = word

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def init_trie(words):
            trie = Trie()
            for w in words:
                trie.insert(w)
            return trie

        def inbound(r, c):
            return 0 <= r < H and 0 <= c < W

        def dfs(r, c, node):
            if not inbound(r, c) or board[r][c] == "#":
                return

            ch = board[r][c]
            if ch not in node.children:
                return

            board[r][c] = "#"
            node = node.children[ch]
            if node.is_word:
                res.add(node.word)

            for i, j in directions:
                dfs(r+i, c+j, node)

            board[r][c] = ch

        trie = init_trie(words)
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        H, W = len(board), len(board[0])
        res = set()

        for i in range(H):
            for j in range(W):
                dfs(i, j, trie.root)

        return list(res)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
                 ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        words = ["oath", "pea", "eat", "rain"]
        expected = ["eat", "oath"]
        self.assertCountEqual(sol.findWords(board, words), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
