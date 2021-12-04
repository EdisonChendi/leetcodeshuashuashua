import unittest
from typing import List
from pprint import pprint
import operator


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=operator.itemgetter(0))
        res, N = 1, len(envelopes)
        dp = [1, ]*N
        for i in range(1, N):
            wi, hi = envelopes[i]
            for j in range(i):
                wj, hj = envelopes[j]
                if wi > wj and hi > hj:
                    dp[i] = max(dp[i], 1+dp[j])
            res = max(res, dp[i])
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
        expected = 3
        self.assertEqual(sol.maxEnvelopes(envelopes), expected)

    def test_case_2(self):
        sol = Solution()
        envelopes = [[1, 1], [1, 1], [1, 1], [1, 1]]
        expected = 1
        self.assertEqual(sol.maxEnvelopes(envelopes), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
