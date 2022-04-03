import functools
import unittest
from typing import List
from pprint import pprint

import functools


class Solution0:
    def numberOfWays(self, s: str) -> int:
        N = len(s)

        # pre process
        number = []
        accu = 1
        for i in range(N):
            if i > 0:
                if s[i] == s[i-1]:
                    accu += 1
                else:
                    number.append((s[i-1], accu))
                    accu = 1
        else:
            number.append((s[N-1], accu))

        @functools.cache
        def dfs(i, last, accu):
            if accu == 3:
                return 1

            if i >= len(number):
                return 0

            return dfs(i+2, last, accu) + number[i][1] * dfs(i+1, number[i][0], accu+1)

        return dfs(0, "", 0) + dfs(1, "", 0)


class Solution:
    def numberOfWays(self, s: str) -> int:
        N = len(s)
        cnt0 = cnt1 = 0
        for n in s:
            cnt0 += n == '0'
            cnt1 += n == '1'
        ans = 0
        cur0 = cur1 = 0
        for n in s:
            cur0 += n == '0'
            cur1 += n == '1'

            if n == '0':
                ans += cur1 * (cnt1 - cur1)
            else:
                ans += cur0 * (cnt0 - cur0)
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "001101"
        expected = 6
        self.assertEqual(sol.numberOfWays(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "11100"
        expected = 0
        self.assertEqual(sol.numberOfWays(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
