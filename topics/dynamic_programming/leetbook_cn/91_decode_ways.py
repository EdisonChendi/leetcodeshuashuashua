import unittest
from typing import List
from pprint import pprint


class Solution1:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp1, dp2 = 1, 1
        for i in range(1, len(s)):
            dp = 0
            prev, ch = s[i-1], s[i]
            if ch == '0':
                if prev == '1' or prev == '2':
                    dp = dp1
            else:
                dp = dp2
                if prev != '0' and 1 <= int(prev+ch) <= 26:
                    dp += dp1
            dp1, dp2 = dp2, dp
        return dp2


class Solution:
    def numDecodings(self, s: str) -> int:

        def valid(s):
            return 1 if s[0] != '0' and 1 <= int(s) <= 26 else 0

        if s[0] == "0":
            return 0

        dp1, dp2 = 1, 1
        for i in range(1, len(s)):
            dp1, dp2 = dp2, dp1*valid(s[i-1]+s[i]) + dp2*valid(s[i])

        return dp2


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
        s = "06"
        expected = 0
        self.assertEqual(sol.numDecodings(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
