import unittest
from typing import List
from pprint import pprint


class Solution:
    def minCut(self, s: str) -> int:
        # dp[i][j] = min(dp[i][k]+dp[k+1][j]) for k in range(i,j)
        cache = {}

        def palindrome(s):
            # needs some 
            if s in cache:
                return cache[s]

            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    cache[s] = False
                    return False
                i += 1
                j -= 1

            cache[s] = True
            return True

        L = len(s)
        dp = [[0]*L for _ in range(L)]
        for i in reversed(range(L)):
            for j in range(i+1, L):
                dp[i][j] = j-i
                if palindrome(s[i:j+1]):
                    dp[i][j] = 0
                    continue
                for k in range(i, j):
                    if palindrome(s[k+1:j+1]):
                        dp[i][j] = min(dp[i][j], dp[i][k]+1)
                    else:
                        dp[i][j] = min(dp[i][j], 1+dp[i][k]+dp[k+1][j])
        return dp[0][-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "aab"
        expected = 1
        self.assertEqual(sol.minCut(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "a"
        expected = 0
        self.assertEqual(sol.minCut(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "aabaa"
        expected = 0
        self.assertEqual(sol.minCut(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "ab"
        expected = 1
        self.assertEqual(sol.minCut(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
