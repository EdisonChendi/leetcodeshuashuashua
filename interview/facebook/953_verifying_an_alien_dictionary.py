import unittest
from typing import List
from pprint import pprint


class Solution1:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def gt(w1, w2):
            i = j = 0
            while i < len(w1) and j < len(w2):
                v1 = ch_order[ord(w1[i])-ord('a')]
                v2 = ch_order[ord(w2[j])-ord('a')]
                if v1 == v2:
                    i, j = i+1, j+1
                    continue
                return v1 > v2
            return i < len(w1)

        ch_order = ['']*26
        for i, ch in enumerate(order):
            ch_order[ord(ch)-ord('a')] = i
        for i in range(len(words)-1):
            if gt(words[i], words[i+1]):
                return False
        return True


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {ch: i for i, ch in enumerate(order)}
        w = [[m[ch] for ch in word] for word in words]
        return all(w[i] <= w[i+1] for i in range(len(w)-1))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        expected = True
        self.assertEqual(sol.isAlienSorted(words, order), expected)

    def test_case_2(self):
        sol = Solution()
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        expected = False
        self.assertEqual(sol.isAlienSorted(words, order), expected)

    def test_case_3(self):
        sol = Solution()
        words = ["apple", "app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        expected = False
        self.assertEqual(sol.isAlienSorted(words, order), expected)

    def test_case_4(self):
        sol = Solution()
        words = ["ubg", "kwh"]
        order = "qcipyamwvdjtesbghlorufnkzx"
        expected = True
        self.assertEqual(sol.isAlienSorted(words, order), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
