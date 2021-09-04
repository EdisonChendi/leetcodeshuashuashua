import unittest
from typing import List
from pprint import pprint

def valid(s):
    return 1 if s[0] != "0" and int(s) < 27 else 0

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0

        s = "0" + s
        dp1, dp2 = 1, 1
        for i in range(2, len(s)):
            dp1, dp2 = dp2, dp1*valid(s[i-1:i+1])+dp2*valid(s[i])
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
        s = "0"
        expected = 0
        self.assertEqual(sol.numDecodings(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "06"
        expected = 0
        self.assertEqual(sol.numDecodings(s), expected)

    def test_case_5(self):
        sol = Solution()
        s = "120"
        expected = 1
        self.assertEqual(sol.numDecodings(s), expected)

    def test_case_6(self):
        sol = Solution()
        s = "1200"
        expected = 0
        self.assertEqual(sol.numDecodings(s), expected)
        
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
