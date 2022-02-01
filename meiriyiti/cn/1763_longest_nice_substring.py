from curses import keyname
import unittest
from typing import List
from pprint import pprint
from copy import copy
from collections import Counter


def valid(d):
    for k in d.keys():
        if d[k] == 0:
            continue
        if k.isupper() and (k.lower() not in d or d[k.lower()] == 0) or \
                k.islower() and (k.upper() not in d or d[k.upper()] == 0):
            return False
    return True


class Solution1:
    def longestNiceSubstring(self, s: str) -> str:
        N = len(s)
        pre_sums = [Counter() for _ in range(N+1)]
        for i, ch in enumerate(s):
            pre_sums[i+1] = copy(pre_sums[i])
            pre_sums[i+1][ch] += 1

        res = ""
        for i in range(N):
            for j in range(i+1+len(res), N+1):
                if valid(pre_sums[j]-pre_sums[i]):
                    if j-i > len(res):
                        res = s[i:j]
        return res


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        L = len(s)
        start = -1
        max_len = 0
        a, A = ord('a'), ord('A')
        for i in range(L):
            l, u = 0, 0
            for j in range(i, L):
                ch = s[j]
                if ch.islower():
                    l |= 1 << ord(ch)-a
                else:
                    u |= 1 << ord(ch)-A
                if l == u and j-i+1 > max_len:
                    start = i
                    max_len = j-i+1
        return s[start:start+max_len]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "YazaAay"
        expected = "aAa"
        self.assertEqual(sol.longestNiceSubstring(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "Bb"
        expected = "Bb"
        self.assertEqual(sol.longestNiceSubstring(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "c"
        expected = ""
        self.assertEqual(sol.longestNiceSubstring(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
