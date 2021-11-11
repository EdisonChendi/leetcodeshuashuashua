import unittest
from typing import List
from pprint import pprint


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # f[i][j] - 1...i, j inverse pairs, ends with k
        # sum for k from 1 -> i, f[i-1][j-(i-k)]
        # i-k <==> 0 -> i-1, ==>
        # sum for k from 0 -> i-1, f[i-1][j-k]
        dp = [0, ]*(k+1)
        pre = [0, ]*(k+1)
        MOD = 10**9 + 7
        for i in range(n+1):
            dp[0] = 1
            pre[0] = 1
            for j in range(1, k+1):
                dp[j] = (pre[j]-(pre[j-i] if j-i >= 0 else 0)) % MOD
            for j in range(1, k+1):
                pre[j] = (pre[j-1] + dp[j]) % MOD
        return dp[k]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        k = 0
        expected = 1
        self.assertEqual(sol.kInversePairs(n, k), expected)

    def test_case_2(self):
        sol = Solution()
        n = 3
        k = 1
        expected = 2
        self.assertEqual(sol.kInversePairs(n, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
