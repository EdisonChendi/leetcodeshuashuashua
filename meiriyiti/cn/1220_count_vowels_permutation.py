import unittest
from typing import List
from pprint import pprint


class Solution1:
    def countVowelPermutation(self, n: int) -> int:
        rules = {
            'x': {'a', 'e', 'i', 'o', 'u'},
            'a': {'e'},
            'e': {'a', 'i'},
            'i': {'a', 'e', 'o', 'u'},
            'o': {'i', 'u'},
            'u': {'a'}
        }
        cache = {}
        MOD = 10 ** 9 + 7

        def helper(ch: str, n: int) -> int:
            if (ch, n) in cache:
                return cache[(ch, n)]

            if n == 0:
                return 1

            res = 0
            for nei in rules[ch]:
                res += helper(nei, n-1)
                res %= MOD
            cache[(ch, n)] = res
            return res

        return helper('x', n)


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # 'a' 'e' 'i' 'o' 'u'
        dp = [1, 1, 1, 1, 1]
        MOD = 10 ** 9 + 7
        for _ in range(n-1):
            dp = (
                (dp[1]+dp[2]+dp[4]) % MOD,
                (dp[0]+dp[2]) % MOD,
                (dp[1]+dp[3]) % MOD,
                dp[2] % MOD,
                (dp[2]+dp[3]) % MOD
            )
        return sum(dp) % MOD


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 1
        expected = 5
        self.assertEqual(sol.countVowelPermutation(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 2
        expected = 10
        self.assertEqual(sol.countVowelPermutation(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 5
        expected = 68
        self.assertEqual(sol.countVowelPermutation(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
