import unittest
from typing import List
from pprint import pprint


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[m][k] - number of floors we can check
        # k: number of eggs
        # m: number of moves
        # dp[m][k] = 1 + dp[m-1][k] + dp[m-1][k-1]
        # if we increase m, dp increases
        #                k, dp increases
        K = k
        dp = [0]*(k+1)
        for m in range(1, n+1):
            nxt_dp = [0]*(K+1)
            for k in range(1, K+1):
                nxt_dp[k] = 1 + dp[k] + dp[k-1]
            dp = nxt_dp
            if dp[-1] >= n:
                return m


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        k = 1
        n = 2
        expected = 2
        self.assertEqual(sol.superEggDrop(k, n), expected)

    def test_case_2(self):
        sol = Solution()
        k = 2
        n = 6
        expected = 3
        self.assertEqual(sol.superEggDrop(k, n), expected)

    def test_case_3(self):
        sol = Solution()
        k = 3
        n = 14
        expected = 4
        self.assertEqual(sol.superEggDrop(k, n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
