import unittest
from typing import List
from pprint import pprint
import collections
import math


class Solution1:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        neighbors = collections.defaultdict(set)
        for s, d in edges:
            neighbors[s].add(d)
            neighbors[d].add(s)

        # BFS simulation
        q = {1}
        step = 0
        dist = [[math.inf, math.inf] for _ in range(n+1)]
        while dist[n][1] == math.inf:
            nxt_q = set()
            while q:
                node = q.pop()
                for nei in neighbors[node]:
                    if step+1 < dist[nei][0]:
                        dist[nei][0] = step+1
                        nxt_q.add(nei)
                    elif dist[nei][0] < step+1 < dist[nei][1]:
                        dist[nei][1] = step+1
                        nxt_q.add(nei)
            q = nxt_q
            step += 1

        ans = 0
        for _ in range(dist[n][1]):
            if ans % (2*change) >= change:
                ans += (2*change) - ans % (2*change)
            ans += time
        return ans


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        neighbors = collections.defaultdict(set)
        for s, d in edges:
            neighbors[s].add(d)
            neighbors[d].add(s)

        q = {1}
        step = 0
        visit = collections.defaultdict(int)
        visit[1] = 1
        while q:
            nxt_q = set()
            while q:
                node = q.pop()
                for nei in neighbors[node]:
                    if nei not in nxt_q and visit[nei] < 2:
                        visit[nei] += 1
                        nxt_q.add(nei)
            q = nxt_q
            step += 1
            if visit[n] == 2:
                break

        ans = 0
        for _ in range(step):
            if ans % (2*change) >= change:
                ans += 2*change - ans % (2*change)
            ans += time
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 5
        edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
        time = 3
        change = 5
        expected = 13
        self.assertEqual(sol.secondMinimum(n, edges, time, change), expected)

    def test_case_2(self):
        sol = Solution()
        n = 2
        edges = [[1, 2]]
        time = 3
        change = 2
        expected = 11
        self.assertEqual(sol.secondMinimum(n, edges, time, change), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
