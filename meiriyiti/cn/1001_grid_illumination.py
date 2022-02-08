import unittest
from typing import List
from pprint import pprint
import collections
import itertools


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        pie = collections.defaultdict(int)
        na = collections.defaultdict(int)
        col = collections.defaultdict(int)
        row = collections.defaultdict(int)
        lamps_ = set()
        for r, c in lamps:
            if (r, c) not in lamps_:
                lamps_.add((r, c))
                pie[r+c] += 1
                na[r-c] += 1
                col[c] += 1
                row[r] += 1

        ans = []

        for r, c in queries:
            if (r+c) in pie and pie[r+c] > 0 \
                    or (r-c) in na and na[r-c] > 0 \
                or c in col and col[c] > 0 \
                    or r in row and row[r] > 0:
                ans.append(1)
            else:
                ans.append(0)
            # query
            for i, j in itertools.product((0, 1, -1), (0, 1, -1)):
                nr, nc = r+i, c+j
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) in lamps_:
                    lamps_.remove((nr, nc))
                    pie[nr+nc] -= 1
                    na[nr-nc] -= 1
                    col[nc] -= 1
                    row[nr] -= 1
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 5
        lamps = [[0, 0], [4, 4]]
        queries = [[1, 1], [1, 0]]
        expected = [1, 0]
        self.assertEqual(sol.gridIllumination(n, lamps, queries), expected)

    def test_case_2(self):
        sol = Solution()
        n = 5
        lamps = [[0, 0], [4, 4]]
        queries = [[1, 1], [1, 1]]
        expected = [1, 1]
        self.assertEqual(sol.gridIllumination(n, lamps, queries), expected)

    def test_case_3(self):
        sol = Solution()
        n = 5
        lamps = [[0, 0], [0, 4]]
        queries = [[0, 4], [0, 1], [1, 4]]
        expected = [1, 1, 0]
        self.assertEqual(sol.gridIllumination(n, lamps, queries), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
