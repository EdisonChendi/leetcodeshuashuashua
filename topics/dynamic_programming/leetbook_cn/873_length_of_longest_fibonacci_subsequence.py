import collections
import unittest
from typing import List
from pprint import pprint


class Solution1:
    # TLE
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        fibs = {tuple(): 0}
        ans = 0
        for i in range(len(arr)):
            v = arr[i]
            new_fibs = {}
            for fib, c in fibs.items():
                if len(fib) == 2:
                    a, b = fib
                    if a+b == v:
                        new_fibs[(b, v)] = max(c+1, new_fibs.get((b, v), 0))
                        ans = max(ans, new_fibs[(b, v)])
                    elif a+b > v:
                        new_fibs[fib] = c
                else:
                    new_fibs[fib] = c
                    new_fibs[fib+(v,)] = c+1
            fibs = new_fibs
        return ans


class Solution2:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # dp[i,j] = dp[k,i]+1 if arr[k]+arr[i] == arr[j]
        N = len(arr)
        ans = 0
        seen = {}
        dp = [[2]*N for _ in range(N)]
        for j in range(N):
            vj = arr[j]
            for i in range(j):
                vi = arr[i]
                vk = vj - vi
                if vk in seen and seen[vk] < i:
                    k = seen[vk]
                    dp[i][j] = dp[k][i]+1
                    ans = max(ans, dp[i][j])
            seen[vj] = j
        return ans if ans >= 3 else 0


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        dp = collections.defaultdict(int)
        for j in range(len(arr)):
            for i in range(j):
                vk = arr[j]-arr[i]
                if vk < arr[i] and vk in s:
                    dp[arr[i], arr[j]] = dp.get((vk, arr[i]), 2) + 1
        return max(dp.values() or [0])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = 5
        self.assertEqual(sol.lenLongestFibSubseq(arr), expected)

    def test_case_2(self):
        sol = Solution()
        arr = [1, 3, 7, 11, 12, 14, 18]
        expected = 3
        self.assertEqual(sol.lenLongestFibSubseq(arr), expected)

    def test_case_3(self):
        sol = Solution()
        arr = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]
        expected = 5
        self.assertEqual(sol.lenLongestFibSubseq(arr), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
