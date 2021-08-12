import unittest
from typing import List
from pprint import pprint


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[1, ]*N for _ in range(N)]
        for i in reversed(range(N-1)):
            dp[i][i+1] = 2 if s[i] == s[i+1] else 1
            for j in range(i+2, N):
                if s[i] == s[j]:
                    dp[i][j] = 2+dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "bbbab"
        expected = 4
        self.assertEqual(sol.longestPalindromeSubseq(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "cbbd"
        expected = 2
        self.assertEqual(sol.longestPalindromeSubseq(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
