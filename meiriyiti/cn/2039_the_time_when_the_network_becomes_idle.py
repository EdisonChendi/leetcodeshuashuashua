from sqlite3 import paramstyle
import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        adj_lists = collections.defaultdict(list)
        for a, b in edges:
            adj_lists[a].append(b)
            adj_lists[b].append(a)

        N = len(patience)
        distance = [0]*N
        visited = {0}
        cur = 0
        q = [0]
        while q:
            nxt_q = []
            while q:
                n = q.pop()
                distance[n] = cur
                for nei in adj_lists[n]:
                    if nei not in visited:
                        nxt_q.append(nei)
                        visited.add(nei)
            q = nxt_q
            cur += 1

        res = 0
        for node in range(1, N):
            t_reply = 2*distance[node]
            p = patience[node]
            t_last_sent = ((t_reply-1)//p)*p  # key
            t_last_reply = t_last_sent+t_reply
            res = max(res, t_last_reply)
        return res+1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        edges = [[0, 1], [1, 2]]
        patience = [0, 2, 1]
        expected = 8
        self.assertEqual(sol.networkBecomesIdle(edges, patience), expected)

    def test_case_2(self):
        sol = Solution()
        edges = [[0, 1], [0, 2], [1, 2]]
        patience = [0, 10, 10]
        expected = 3
        self.assertEqual(sol.networkBecomesIdle(edges, patience), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
