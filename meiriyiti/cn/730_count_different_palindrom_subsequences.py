import unittest
from typing import List
from pprint import pprint

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        # dp[ch][i][j]
        # in substring range [i,j]
        # ch - a/b/c/d
        # number of palindrome subsequnces that begins with ch
        if not s:
            return 0

        MOD = 10**9 + 7
        L = len(s)
        dp = [[[0]*L for _ in range(L)] for _ in range(4)]
        orda = ord('a')
        for i,ch in enumerate(s):
            dp[ord(ch)-orda][i][i] = 1

        for i in reversed(range(L-1)):
            for j in range(i+1, L):
                for ch in 'abcd':
                    if s[i] == ch and s[j] == ch:
                        dp[ord(ch)-orda][i][j] = (2 + sum(dp[ord(k)-orda][i+1][j-1] for k in 'abcd'))%MOD if j - i > 1 else 2
                    elif s[i] == ch:
                        dp[ord(ch)-orda][i][j] = dp[ord(ch)-orda][i][j-1] 
                    elif s[j] == ch:
                        dp[ord(ch)-orda][i][j] = dp[ord(ch)-orda][i+1][j] 
                    else:
                        dp[ord(ch)-orda][i][j] = dp[ord(ch)-orda][i+1][j-1] if j - i > 1 else 0
        return sum(d[0][L-1] for d in dp) % MOD

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "bccb"
        expected = 6
        self.assertEqual(sol.countPalindromicSubsequences(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
        expected = 104860361
        self.assertEqual(sol.countPalindromicSubsequences(s), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
