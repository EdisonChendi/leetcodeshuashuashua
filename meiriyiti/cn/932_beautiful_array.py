import unittest
from typing import List
from pprint import pprint

import collections


class Solution1:
    # LTE(very quickly)
    def beautifulArray(self, n: int) -> List[int]:
        ans = []
        disabled = collections.Counter()

        def dfs(choices, i):
            for i, ch in enumerate(choices):
                if ch in disabled and disabled[ch] > 0:
                    continue

                ans.append(ch)
                if len(ans) == n:
                    return True
                for j in range(len(ans)-1):
                    nj = ans[j]
                    disabled[2*ch-nj] += 1

                found = dfs(choices[:i]+choices[i+1:], i+1)
                if found:
                    return found

                ans.pop()
                for i in range(len(ans)):
                    ni = ans[i]
                    disabled[2*ch-ni] -= 1

            return False

        dfs(list(range(1, n+1)), 0)
        return ans


class Solution2:
    # dp - pass - O(n^2)
    def beautifulArray(self, n: int) -> List[int]:
        dp = [[], [1], ]
        for i in range(2, n+1):
            l = (i+1)//2
            r = i//2
            dp.append([2*j-1 for j in dp[l]]+[2*k for k in dp[r]])
        return dp[-1]


class Solution3:
    # divide and conque - O(NlgN)
    def beautifulArray(self, n: int) -> List[int]:
        cache = {1: [1]}

        def solve(n: int) -> List[int]:
            print(n)
            if n in cache:
                return cache[n]

            left = solve((n+1)//2)  # odd
            right = solve(n//2)  # even
            res = [2*l-1 for l in left] + [2*r for r in right]
            cache[n] = res
            return res

        return solve(n)


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            cur = []
            for v in res:
                if 2*v-1 <= n:
                    cur.append(2*v-1)
            for v in res:
                if 2*v <= n:
                    cur.append(2*v)
            res = cur
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 100
        print(sol.beautifulArray(n))

    def test_case_2(self):
        sol = Solution()
        n = 5
        print(sol.beautifulArray(n))

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
