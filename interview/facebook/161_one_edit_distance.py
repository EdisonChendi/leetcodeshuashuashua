import unittest
from typing import List
from pprint import pprint


class Solution1:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        def check_insert(s, t):
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    j += 1
                else:
                    i += 1
                    j += 1
            return j-i <= 1

        def check_replace(s, t):
            op = False
            for i in range(len(s)):
                if s[i] != t[i]:
                    if op:
                        return False
                    op = True
            return op

        if len(s) >= len(t):
            s, t = t, s

        if len(t) - len(s) > 1:
            return False

        if len(s) == len(t):
            return check_replace(s, t)

        return check_insert(s, t)


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        ns, nt = len(s), len(t)

        if ns > nt:
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] == t[i]:
                continue

            if nt == ns:
                return s[i+1:] == t[i+1:]
            else:
                return s[i:] == t[i+1:]

        return nt - ns == 1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "ab"
        t = "acb"
        expected = True
        self.assertEqual(sol.isOneEditDistance(s, t), expected)

    def test_case_2(self):
        sol = Solution()
        s = ""
        t = ""
        expected = False
        self.assertEqual(sol.isOneEditDistance(s, t), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
