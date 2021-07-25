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


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)

        M, N, res = len(board), len(board[0]), set()

        def in_bound(i, j):
            return 0 <= i < M and 0 <= j < N

        def dfs(node, accu, i, j, res):
            if not in_bound(i, j) or board[i][j] == "#" or board[i][j] not in node.children:
                return

            ch, board[i][j] = board[i][j], "#"
            accu, node = accu+ch, node.children[ch]
            if node.end_of_word:
                res.add(accu)

            for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                dfs(node, accu, ni, nj, res)

            board[i][j] = ch

        for i in range(M):
            for j in range(N):
                dfs(trie.root, "", i, j, res)

        return list(res)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [["o", "a", "a", "n"],
                 ["e", "t", "a", "e"],
                 ["i", "h", "k", "r"],
                 ["i", "f", "l", "v"]]
        words = ["oath", "pea", "eat", "rain"]
        expected = ["eat", "oath"]
        self.assertCountEqual(sol.findWords(board, words), expected)

    def test_case_2(self):
        sol = Solution()
        board = [["a", "b"], ["c", "d"]]
        words = ["abcb"]
        expected = []
        self.assertCountEqual(sol.findWords(board, words), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
