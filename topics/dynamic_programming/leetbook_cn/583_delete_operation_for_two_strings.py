import unittest
from typing import List
from pprint import pprint


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # state transition functions:
        # dp[i][j], i: word1 index, j: word2 index
        # dp[i][j] = dp[i-1][j-1] if word1[i] == word2[j] else 1 + min(dp[i-1][j], dp[i][j-1])
        L1, L2 = len(word1), len(word2)
        dp = list(range(L2+1))
        for i in range(1, L1+1):
            new_dp = [i, ] + dp[1:]
            for j in range(1, L2+1):
                if word1[i-1] == word2[j-1]:
                    new_dp[j] = dp[j-1]
                else:
                    new_dp[j] = min(1+dp[j], 1+new_dp[j-1], 2+dp[j-1])
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

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
