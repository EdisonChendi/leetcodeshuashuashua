import unittest
from typing import List
from pprint import pprint
import collections


class Solution:

    def tarjan_scc(self, edges):
        # return List[List[int]]
        adjlists = collections.defaultdict(list)
        for s, d in edges:
            adjlists[s].append(d)
        n = len(adjlists.keys())

        stack = []
        on_stack = [False]*n
        visited = [False]*n
        sccs = []
        ids = [-1]*n
        lows = [-1]*n
        cur_id = 0

        def dfs(i):
            nonlocal cur_id
            stack.append(i)
            on_stack[i] = True
            visited[i] = True
            ids[i] = cur_id
            lows[i] = cur_id
            cur_id += 1

            for nei in adjlists[i]:
                if not visited[nei]:
                    dfs(nei)
                if on_stack[nei]:
                    lows[i] = min(lows[i], lows[nei])

            if lows[i] == ids[i]:
                scc = []
                while True:
                    node = stack.pop()
                    on_stack[node] = False
                    # lows[node] = ids[i] # not necessary
                    scc.append(node)
                    if node == i:
                        break
                sccs.append(scc)

        for node in range(n):
            if not visited[node]:
                dfs(node)

        return sccs


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        edges = [(6, 0),
                 (6, 2),
                 (3, 4),
                 (6, 4),
                 (2, 0),
                 (0, 1),
                 (4, 5),
                 (5, 6),
                 (3, 7),
                 (7, 5),
                 (1, 2),
                 (7, 3),
                 (5, 0)]
        sccs = sol.tarjan_scc(edges)
        print(sccs)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
