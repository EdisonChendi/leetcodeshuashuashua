import unittest
from typing import List
from pprint import pprint


class Solution:
    def numTrees(self, n: int) -> int:
        # dp[n] = dp[0]*dp[n-1]+dp[1]*dp[n-2]+...+dp[k]*dp[n-k-1]+...+dp[n-1]*dp[0]
        # dp[1] = 1
        # dp[0] = 1
        # dp[2] = 2
        # dp[3] = 1*2 + 1 + 2*1 = 5
        dp = [0,]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2,n+1):
            dp[i] = sum(dp[k]*dp[i-k-1] for k in range(0,i))
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        expected = 5
        self.assertEqual(sol.numTrees(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        expected = 1
        self.assertEqual(sol.numTrees(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 2
        expected = 2
        self.assertEqual(sol.numTrees(n), expected)
        
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
