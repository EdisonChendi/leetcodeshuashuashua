import unittest
from typing import List
from pprint import pprint


class Solution:
    def minCut(self, s: str) -> int:
        # dp[i][j] = min(dp[i][k]+dp[k+1][j]) for k in range(i,j)
        cache = {}

        def palindrome(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= j:
                return True
            if s[i] == s[j]:
                res = palindrome(i+1,j-1)
            else:
                res = False
            cache[(i,j)] = res
            return res


        L = len(s)
        dp = [0,]*L

        for j in range(L):
            if palindrome(0,j):
                dp[j] = 0
            else:
                dp[j] = min(1+dp[i-1] for i in range(1,j+1) if palindrome(i,j))
            
        
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
