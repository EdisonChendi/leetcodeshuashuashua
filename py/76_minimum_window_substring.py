import unittest
from typing import List
from pprint import pprint
from collections import Counter, deque, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""

        win = deque()
        win_counter = defaultdict(int)
        t_counter = Counter(t)
        t_counter2 = Counter(t)
        res = s+" "

        for ch in s:
            win.append(ch)
            win_counter[ch] += 1
            if ch in t_counter:
                if ch in t_counter2:
                    t_counter2[ch] -= 1
                    if t_counter2[ch] == 0:
                        t_counter2.pop(ch)
                while win and ((win[0] in t_counter and win_counter[win[0]] > t_counter[win[0]])
                               or (win[0] not in t_counter)):
                    win_counter[win.popleft()] -= 1

            if not t_counter2 and len(win) < len(res):
                res = "".join(win)

        return "" if len(res) > m else res


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
