import unittest
from typing import List
from pprint import pprint

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0,]*(l2+1) for _ in range(l1+1)]
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        text1 = "abcde"; text2 = "ace" 
        expected = 3
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), expected)

    def test_case_2(self):
        sol = Solution()
        text1 = "abc"; text2 = "abc"
        expected = 3
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), expected)

    def test_case_3(self):
        sol = Solution()
        text1 = "abc"; text2 = "def"
        expected = 0
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), expected)
        
    def test_edge_case_1(self):
        s = Solution()
        sol = Solution()
        text1 = "a"; text2 = "a"
        expected = 1
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), expected)

    def test_edge_case_2(self):
        s = Solution()
        sol = Solution()
        text1 = "a"; text2 = "b"
        expected = 0
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), expected)


if __name__ == "__main__":
    unittest.main()
