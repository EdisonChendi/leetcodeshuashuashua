import unittest
from typing import List
from pprint import pprint

import collections


class TrieNode:

    def __init__(self) -> None:
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys = keys
        self.keys_m = {k: i for i, k in enumerate(keys)}
        self.values = values
        self.values_m = collections.defaultdict(list)
        for i, v in enumerate(values):
            self.values_m[v].append(i)
        self.dictionary = dictionary
        self.trie = Trie()
        for word in dictionary:
            self.trie.insert(word)

    def encrypt(self, word1: str) -> str:
        res = []
        for ch in word1:
            res.append(self.values[self.keys_m[ch]])
        return "".join(res)

    def decrypt(self, word2: str) -> int:
        N = len(word2)
        res = 0

        def dfs(trie_node, i):
            nonlocal res
            if i == N:
                res += trie_node.is_word
                return

            two_ch = word2[i:i+2]
            valid_indices = self.values_m[two_ch]
            # print(two_ch, valid_indices)
            for idx in valid_indices:
                ch = self.keys[idx]
                # print(two_ch, valid_indices, ch)
                if ch in trie_node.children:
                    # print(two_ch, valid_indices, ch, i)
                    dfs(trie_node.children[ch], i+2)

        dfs(self.trie.root, 0)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        enc = Encrypter(['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], [
                        "abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])
        ans1 = enc.encrypt("abcd")
        expect1 = "eizfeiam"
        self.assertEqual(ans1, expect1)
        ans2 = enc.decrypt("eizfeiam")
        expect2 = 2
        self.assertEqual(ans2, expect2)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
