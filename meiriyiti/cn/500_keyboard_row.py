import unittest
from typing import List
from pprint import pprint


def same(l):
    if not l:
        return False
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            return False
    return True


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboards = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        keys = {k: i for i, ks in enumerate(keyboards) for k in ks}
        return [w for w in words if same([keys[ch] for ch in w.lower()])]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        words = ["Hello", "Alaska", "Dad", "Peace"]
        expected = ["Alaska", "Dad"]
        self.assertCountEqual(sol.findWords(words), expected)

    def test_case_2(self):
        sol = Solution()
        words = ["omk"]
        expected = []
        self.assertCountEqual(sol.findWords(words), expected)

    def test_case_3(self):
        sol = Solution()
        words = ["adsdf", "sfd"]
        expected = ["adsdf", "sfd"]
        self.assertCountEqual(sol.findWords(words), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
