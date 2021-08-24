import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # use bellman-ford algorithm

        dp = [math.inf, ]*n
        dp[src] = 0
        for _ in range(k+1):
            new_dp = dp[:]
            for f, t, w in flights:
                new_dp[t] = min(new_dp[t], dp[f]+w)
            dp = new_dp
        return dp[dst] if dp[dst] != math.inf else -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        expected = 200
        self.assertEqual(sol.findCheapestPrice(
            n, flights, src, dst, k), expected)

    def test_case_2(self):
        sol = Solution()
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        expected = 500
        self.assertEqual(sol.findCheapestPrice(
            n, flights, src, dst, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
