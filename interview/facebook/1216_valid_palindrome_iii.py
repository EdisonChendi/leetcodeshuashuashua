import unittest
from typing import List
from pprint import pprint

import functools


class Solution1:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        @functools.cache
        def dfs(i, j, k):

            if k < 0:
                return False

            if i >= j:
                return True

            if s[i] == s[j] and dfs(i+1, j-1, k):
                return True
            else:
                return dfs(i+1, j, k-1) or dfs(i, j-1, k-1)

        return dfs(0, len(s)-1, k)


class Solution2:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # Top-Down DP

        @functools.cache
        def min_removes(i, j):
            if i >= j:
                return 0

            if s[i] == s[j]:
                return min_removes(i+1, j-1)
            else:
                return 1+min(min_removes(i+1, j), min_removes(i, j-1))

        return min_removes(0, len(s)-1) <= k


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        N = len(s)
        dp = [0]*N
        for i in reversed(range(N-1)):
            new_dp = [0]*N
            for j in range(i+1, N):
                if s[i] == s[j]:
                    new_dp[j] = dp[j-1]
                else:
                    new_dp[j] = 1 + min(new_dp[j-1], dp[j])
            dp = new_dp
        return dp[-1] <= k


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "abcdeca"
        k = 2
        expected = True
        self.assertEqual(sol.isValidPalindrome(s, k), expected)

    def test_case_2(self):
        sol = Solution()
        s = "abbababa"
        k = 1
        expected = True
        self.assertEqual(sol.isValidPalindrome(s, k), expected)

    def test_case_3(self):
        sol = Solution()
        s = "aaabaabaa"
        k = 1
        expected = True
        self.assertEqual(sol.isValidPalindrome(s, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
