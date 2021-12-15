import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """
        topological sort
        """
        N = len(quiet)
        g = collections.defaultdict(list)
        indgree = [0]*N
        res = list(range(N))
        for a, b in richer:
            g[a].append(b)
            indgree[b] += 1

        q = collections.deque(i for i in range(N) if indgree[i] == 0)

        while q:
            a = q.popleft()
            for b in g[a]:
                if quiet[res[a]] < quiet[res[b]]:
                    res[b] = res[a]
                if indgree[b] > 0:
                    indgree[b] -= 1
                    if indgree[b] == 0:
                        q.append(b)
        return res


class Solution1:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """
        dfs
        """
        N = len(quiet)
        ans = [0]*N
        visited = {}

        def dfs(p):
            if p in visited:
                return visited[p]

            if p not in g:
                res = (quiet[p], p)
            else:
                res = min(min(dfs(r) for r in g[p]), (quiet[p], p))

            visited[p] = res
            ans[p] = res[1]
            return res

        g = collections.defaultdict(list)
        for a, b in richer:
            g[b].append(a)

        for n in range(N):
            dfs(n)

        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
        quiet = [3, 2, 5, 4, 6, 1, 7, 0]
        expected = [5, 5, 2, 5, 4, 5, 6, 7]
        self.assertListEqual(sol.loudAndRich(richer, quiet), expected)

    def test_case_2(self):
        sol = Solution()
        richer = []
        quiet = [0]
        expected = [0]
        self.assertListEqual(sol.loudAndRich(richer, quiet), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
