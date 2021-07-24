import unittest
from typing import List
from pprint import pprint
from collections import Counter, deque, defaultdict
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""

        needs, missing = Counter(t), len(t)
        i, I, J = 0, 0, 0
        for j, ch in enumerate(s, 1):
            missing -= needs[ch] > 0
            needs[ch] -= 1
            if not missing:
                while i < j and needs[s[i]] < 0:
                    needs[s[i]] += 1
                    i += 1
                if J == 0 or j-i < J-I:
                    I,J = i,j

        return s[I:J]


    def minWindow1(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""

        win = deque()
        win_counter = defaultdict(int)
        t_counter = Counter(t)
        t_counter2 = Counter(t)
        l, r = 0, m

        for i, ch in enumerate(s):
            if ch in t_counter:
                win.append((i, ch))
                win_counter[ch] += 1
                if ch in t_counter2:
                    t_counter2[ch] -= 1
                    if t_counter2[ch] == 0:
                        t_counter2.pop(ch)
                while win and (win[0][1] in t_counter and win_counter[win[0][1]] > t_counter[win[0][1]]):
                    win_counter[win.popleft()[1]] -= 1

            if not t_counter2 and (win[-1][0]-win[0][0] < (r-l)):
                r, l = win[-1][0], win[0][0]

        return "" if r-l == m else s[l:r+1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"
        self.assertEqual(sol.minWindow(s, t), expected)

    def test_case_2(self):
        sol = Solution()
        s = "a"
        t = "a"
        expected = "a"
        self.assertEqual(sol.minWindow(s, t), expected)

    def test_case_3(self):
        sol = Solution()
        s = "a"
        t = "aa"
        expected = ""
        self.assertEqual(sol.minWindow(s, t), expected)

    def test_case_4(self):
        sol = Solution()
        s = "aab"
        t = "aab"
        expected = "aab"
        self.assertEqual(sol.minWindow(s, t), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
