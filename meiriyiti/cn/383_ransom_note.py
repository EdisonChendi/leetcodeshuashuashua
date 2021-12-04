import unittest
from typing import List
from pprint import pprint
import collections


class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        if len(r) > len(m):
            return False
        return all((ch in m and m[ch] >= n) for ch, n in r.items())


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        m = [0, ]*26
        for ch in magazine:
            m[ord(ch)-ord('a')] += 1
        for ch in ransomNote:
            pos = ord(ch)-ord('a')
            if m[pos] > 0:
                m[pos] -= 1
            else:
                return False
        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        ransomNotes = "a"
        magazine = "b"
        expected = False
        self.assertEqual(sol.canConstruct(ransomNotes, magazine), expected)

    def test_case_2(self):
        sol = Solution()
        ransomNotes = "aa"
        magazine = "ab"
        expected = False
        self.assertEqual(sol.canConstruct(ransomNotes, magazine), expected)

    def test_case_3(self):
        sol = Solution()
        ransomNotes = "aa"
        magazine = "aab"
        expected = True
        self.assertEqual(sol.canConstruct(ransomNotes, magazine), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
