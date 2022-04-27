import unittest
from typing import List
from pprint import pprint


class Solution1:
    def rotatedDigits(self, n: int) -> int:
        # Brute force
        # Time: O(nlg[10]n)
        # Space: O(lg[10]n)
        D = {'2', '5', '6',  '9', '1', '0', '8'}
        S = {'1', '0', '8'}
        res = 0
        for i in range(1, n+1):
            s = set(str(i))
            if len(s-D) == 0 and len(s-S) > 0:
                res += 1
        return res


class Solution:
    def rotatedDigits(self, n: int) -> int:
        # DP
        # transition function:
        # dp[i] = False if
        #       = True else
        # 0 - bad
        # 1 - normal
        # 2 - good
        dp = [0]*(n+1)
        dp[:10] = [1, 1, 2, 0, 0, 2, 2, 0, 1, 2]
        ans = 0
        for i in range(1, n+1):
            prv, last = divmod(i, 10)
            if dp[last] == 2:
                if dp[prv] != 0:
                    dp[i] = 2
                    ans += 1
                else:
                    dp[i] = 0
            elif dp[last] == 1:
                if dp[prv] == 2:
                    dp[i] = 2
                    ans += 1
                elif dp[prv] == 1:
                    dp[i] = 1
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
