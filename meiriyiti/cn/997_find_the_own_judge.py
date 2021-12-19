import unittest
from typing import List
from pprint import pprint
import collections


class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1
        candidates = {i: set() for i in range(1, n+1)}
        for a, b in trust:
            if b in candidates:
                candidates[b].add(a)
            if a in candidates:
                candidates.pop(a)

        if len(candidates) == 1:
            judge, people = candidates.popitem()
            return judge if len(people) == n-1 else -1
        else:
            return -1


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1
        indegrees = collections.defaultdict(int)
        outdegrees = collections.defaultdict(int)
        for a, b in trust:
            indegrees[b] += 1
            outdegrees[a] += 1
        zero_indegrees = set(list(range(1, n+1))) - outdegrees.keys()
        if len(zero_indegrees) == 1:
            judge = zero_indegrees.pop()
            return judge if indegrees[judge] == n-1 else -1
        else:
            return -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        trust = [[1, 3], [2, 3], [3, 1]]
        expected = -1
        self.assertEqual(sol.findJudge(n, trust), expected)

    def test_case_2(self):
        sol = Solution()
        n = 2
        trust = [[1, 2]]
        expected = 2
        self.assertEqual(sol.findJudge(n, trust), expected)

    def test_case_3(self):
        sol = Solution()
        n = 3
        trust = [[1, 3], [2, 3]]
        expected = 3
        self.assertEqual(sol.findJudge(n, trust), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
