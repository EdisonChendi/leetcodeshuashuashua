import unittest
from typing import List
from pprint import pprint


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # N - length of input string
        # time: O(N^2)
        # space: O(N)
        N = len(s)
        dp = [0]*N
        for i in reversed(range(N-1)):
            nxt_dp = [0]*N
            for j in range(i+1, N):
                if s[i] == s[j]:
                    nxt_dp[j] = dp[j-1]
                else:
                    nxt_dp[j] = 1 + min(nxt_dp[j-1], dp[j])
            dp = nxt_dp
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

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
