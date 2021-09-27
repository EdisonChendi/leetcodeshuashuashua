import unittest
from typing import List
from pprint import pprint


def valid1(s):
    if s == "*":
        return 9
    else:
        return 1 if s != '0' else 0


def valid2(prev, cur):
    if prev != "*" and cur != "*":
        return 1 if prev != '0' and int(prev+cur) <= 26 else 0

    if prev == "*" and cur == "*":
        return 15

    if prev == "*" and cur != "*":
        if int(cur) > 6:
            return 1
        else:
            return 2

    if prev != "*" and cur == "*":
        if prev == '0':
            return 0
        else:
            if int(prev) >= 3:
                return 0
            if prev == '2':
                return 6
            else:
                return 9


class Solution:
    def numDecodings(self, s: str) -> int:
        assert len(s) > 0
        if s[0] == '0':
            return 0
        f2, f1 = 1, 9 if s[0] == '*' else 1
        for i in range(1, len(s)):
            prev, cur = s[i-1], s[i]
            f2, f1 = f1 % (10**9 + 7), (f2*valid2(prev, cur) +
                                        f1*valid1(cur)) % (10**9 + 7)
        return f1 % (10**9 + 7)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "*"
        expected = 9
        self.assertEqual(sol.numDecodings(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "1*"
        expected = 18
        self.assertEqual(sol.numDecodings(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "2*"
        expected = 15
        self.assertEqual(sol.numDecodings(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
