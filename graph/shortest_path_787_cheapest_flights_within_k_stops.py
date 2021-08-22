from math import exp
import unittest
from typing import List
from pprint import pprint
import math
import collections


class Solution:
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def build_rev_graph(flights):
            res = collections.defaultdict(dict)
            for s, d, w in flights:
                res[d][s] = w
            return res

        dp = [math.inf, ]*n
        dp[src] = 0

        rev_graph = build_rev_graph(flights)  # find all src by dst, graph[dst]

        for _ in range(k+1):
            new_dp = dp[:]
            for d in range(n):
                for s, w in rev_graph[d].items():
                    new_dp[d] = min(new_dp[d], dp[s]+w)
            dp = new_dp

        return dp[dst] if dp[dst] != math.inf else -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # no rev_graph

        dp = [math.inf, ]*n
        dp[src] = 0

        for _ in range(k+1):
            new_dp = dp[:]
            for s, d, w in flights:
                new_dp[d] = min(new_dp[d], dp[s]+w)
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
        res = sol.findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(res, expected)

    def test_case_2(self):
        sol = Solution()
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        expected = 500
        res = sol.findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(res, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
