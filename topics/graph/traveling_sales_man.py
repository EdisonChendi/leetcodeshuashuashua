import unittest
from typing import List
from pprint import pprint

import math


class Solution:

    def tsp(self, edges, n, starting):
        # O(n^2*(2**n))
        # dp[city][travelled cities]
        # = dp[n][travlled cities - n]+dist[n][city] for n in all_cities

        def setup():
            matrix = [[math.inf]*n for _ in range(n)]
            matrix[starting][starting] = 0
            for s, d, w in edges:
                matrix[s][d] = w

            memo = [[math.inf]*(2**n) for _ in range(n)]
            for i in range(n):
                if i == starting:
                    continue
                memo[i][(1 << starting) | (1 << i)] = matrix[starting][i]

            return memo, matrix

        def comb(cnt, n):
            res = []

            def backtrack(i, pos, v):
                if i == cnt:
                    res.append(v)
                    return

                for idx in range(pos, n):
                    v |= (1 << idx)
                    backtrack(i+1, idx+1, v)
                    v ^= (1 << idx)

            backtrack(0, 0, 0)
            return res

        def get_tour(memo, matrix):
            res = [starting] + [-1]*(n-1) + [starting]
            last_idx = starting
            travelled = (1 << n) - 1
            for i in reversed(range(1, n)):
                idx = -1
                for j in range(n):
                    if j == starting or ((1 << j) & travelled) == 0:
                        continue
                    if idx == -1:
                        idx = j
                    cur_dist = memo[idx][travelled] + matrix[idx][last_idx]
                    new_dist = memo[j][travelled] + matrix[j][last_idx]
                    if new_dist < cur_dist:
                        idx = j
                res[i] = idx
                travelled ^= (1 << idx)
                last_idx = idx
            return res

        memo, matrix = setup()

        # solve
        for ones in range(3, n+1):
            for travelled in comb(ones, n):
                if (1 << starting) & travelled == 0:
                    continue
                for cur in range(n):
                    if cur == starting or ((1 << cur) & travelled) == 0:
                        continue
                    prv_travelled = travelled ^ (1 << cur)
                    min_ = math.inf
                    for e in range(n):
                        if ((1 << e) & prv_travelled) == 0 or e == starting or e == cur:
                            continue
                        nd = memo[e][prv_travelled] + matrix[e][cur]
                        if nd < min_:
                            min_ = nd
                    memo[cur][travelled] = min_

        # find the min dist
        min_cost = min((memo[i][(1 << n)-1] + matrix[i][starting])
                       for i in range(n) if i != starting)

        # find the tour
        tour = get_tour(memo, matrix)

        return min_cost, tour


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        edges = [
            (5, 0, 10),
            (1, 5, 12),
            (4, 1, 2),
            (2, 4, 4),
            (3, 2, 6),
            (0, 3, 8)
        ]
        n = 6
        starting = 0
        res_min_cost, res_tour = sol.tsp(edges, n, starting)
        expected_min_cost, expected_tour = 42, [0, 3, 2, 4, 1, 5, 0]
        self.assertEqual(res_min_cost, expected_min_cost)
        self.assertListEqual(res_tour, expected_tour)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
