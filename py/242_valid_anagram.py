import unittest
from typing import List
from pprint import pprint

from collections import Counter, defaultdict


class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = defaultdict(int)
        for ch1, ch2 in zip(s, t):
            counter[ch1] -= 1
            counter[ch2] += 1
        return all(v == 0 for v in counter.values())


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "anagram"
        t = "nagaram"
        self.assertTrue(sol.isAnagram(s, t))

    def test_case_2(self):
        sol = Solution()
        s = "rat"
        t = "car"
        self.assertFalse(sol.isAnagram(s, t))

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
