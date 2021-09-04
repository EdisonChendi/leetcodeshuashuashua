import unittest
from typing import List
from pprint import pprint


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = list(range(l2+1))
        for i in range(1, l1+1):
            new_dp = [i, ]+[0, ]*l2
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    new_dp[j] = dp[j-1]
                else:
                    new_dp[j] = 1 + min(dp[j], dp[j-1], new_dp[j-1])
            dp = new_dp
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        word1 = "horse"
        word2 = "ros"
        expected = 3
        self.assertEqual(sol.minDistance(word1, word2), expected)

    def test_case_2(self):
        sol = Solution()
        word1 = "intention"
        word2 = "execution"
        expected = 5
        self.assertEqual(sol.minDistance(word1, word2), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
