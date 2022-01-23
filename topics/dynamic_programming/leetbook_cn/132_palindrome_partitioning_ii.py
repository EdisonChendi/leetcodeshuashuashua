import unittest
from typing import List
from pprint import pprint


class Solution1:
    def minCut(self, s: str) -> int:
        # dp[i][j] = min(dp[i][k]+dp[k+1][j]) for k in range(i,j)
        cache = {}

        def palindrome(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= j:
                return True
            if s[i] == s[j]:
                res = palindrome(i+1, j-1)
            else:
                res = False
            cache[(i, j)] = res
            return res

        L = len(s)
        dp = [0, ]*L

        for j in range(L):
            if palindrome(0, j):
                dp[j] = 0
            else:
                dp[j] = min(1+dp[i-1]
                            for i in range(1, j+1) if palindrome(i, j))

        return dp[-1]


class Solution:
    def minCut(self, s: str) -> int:
        L = len(s)
        palindrome = [[True]*L for _ in range(L)]
        for i in reversed(range(L)):
            for j in range(i+1, L):
                palindrome[i][j] = s[j] == s[i] and \
                    (j == i+1 or palindrome[i+1][j-1])

        dp = list(range(L))
        for i in range(1, L):
            if palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = min(1+dp[j-1]
                            for j in range(1, i+1) if palindrome[j][i])
        return dp[-1]


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
