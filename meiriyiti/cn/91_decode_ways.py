import unittest
from typing import List
from pprint import pprint


def valid(s):
    return 1 if s[0] != '0' and int(s) <= 26 else 0


class Solution:
    def numDecodings(self, s: str) -> int:
        assert len(s) > 0
        if s[0] == '0':
            return 0
        f2, f1 = 1, 1
        for i in range(1, len(s)):
            prev, cur = s[i-1], s[i]
            f2, f1 = f1, f2*valid(prev+cur)+f1*valid(cur)
        return f1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "12"
        expected = 2
        self.assertEqual(sol.numDecodings(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "226"
        expected = 3
        self.assertEqual(sol.numDecodings(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "0"
        expected = 0
        self.assertEqual(sol.numDecodings(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "06"
        expected = 0
        self.assertEqual(sol.numDecodings(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
