import unittest
from typing import List
from pprint import pprint


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1), len(word2)
        dp = list(range(L1+1))
        for j in range(L2):
            new_dp = dp[:]
            new_dp[0] = j+1
            for i in range(1, L1+1):
                if word1[i-1] == word2[j]:
                    new_dp[i] = dp[i-1]
                else:
                    new_dp[i] = 1 + min(dp[i], new_dp[i-1])
            dp = new_dp
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        word1 = "sea"
        word2 = "eat"
        expected = 2
        self.assertEqual(sol.minDistance(word1, word2), expected)

    def test_case_2(self):
        sol = Solution()
        word1 = "leetcode"
        word2 = "etco"
        expected = 4
        self.assertEqual(sol.minDistance(word1, word2), expected)

    def test_case_3(self):
        sol = Solution()
        word1 = "a"
        word2 = "b"
        expected = 2
        self.assertEqual(sol.minDistance(word1, word2), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
