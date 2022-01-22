import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 2:
            return len(arr) - 1

        step = 0
        q = [0]
        L = len(arr)
        visited = [False]*L
        mapping = collections.defaultdict(list)

        for i, n in enumerate(arr):
            mapping[n].append(i)

        while q:
            nxt_q = []
            while q:
                i = q.pop()
                if i == L-1:
                    return step
                n = arr[i]
                for pos in mapping[n]:
                    if not visited[pos]:
                        nxt_q.append(pos)
                        visited[pos] = True
                if i > 0 and not visited[i-1]:
                    visited[i-1] = True
                    nxt_q.append(i-1)
                if i < L-1 and not visited[i+1]:
                    visited[i+1] = True
                    nxt_q.append(i+1)
                del mapping[n]
            step += 1
            q = nxt_q


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
        expected = 3
        self.assertEqual(sol.minJumps(arr), expected)

    def test_case_2(self):
        sol = Solution()
        arr = [7, 6, 9, 6, 9, 6, 9, 7]
        expected = 1
        self.assertEqual(sol.minJumps(arr), expected)

    def test_case_3(self):
        sol = Solution()
        arr = [7]
        expected = 0
        self.assertEqual(sol.minJumps(arr), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
