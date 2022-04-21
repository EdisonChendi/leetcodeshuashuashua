import functools
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        pos = {
            '1': '86',
            '2': '79',
            '3': '48',
            '4': '039',
            '5': '',
            '6': '017',
            '7': '26',
            '8': '13',
            '9': '24',
            '0': '46',
            '!': "0123456789"
        }
        cur = '!'

        @functools.cache
        def dfs(cur, i):
            print(cur, i)
            if i == n:
                return 1
            return sum(dfs(nxt, i+1) for nxt in pos[cur])

        return dfs(cur, 0) % MOD


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        cur = {10}
        dp = [0] * 10 + [1]
        pos = {
            1: [8, 6],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
            10: list(range(10))
        }
        for _ in range(n):
            nxt_dp = [0]*10
            nxt = set()
            for n in cur:
                for t in pos[n]:
                    nxt_dp[t] += dp[n]
                    nxt.add(t)
            dp = nxt_dp
            cur = nxt
        return sum(dp) % MOD


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 1
        expected = 10
        self.assertEqual(sol.knightDialer(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 2
        expected = 20
        self.assertEqual(sol.knightDialer(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 3131
        expected = 136006598
        self.assertEqual(sol.knightDialer(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
