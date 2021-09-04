import unittest
from typing import List
from pprint import pprint
import math
import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def max_sum_1d(col):
            accu, res = 0, -math.inf
            seen = [0, ]
            for n in col:
                accu += n
                comp = accu - k
                idx = bisect.bisect_left(seen, comp)
                if idx != len(seen):
                    if seen[idx] == comp:
                        return k
                    else:
                        res = max(res, accu-seen[idx])
                bisect.insort_left(seen, accu)
            return res

        m, n = len(matrix), len(matrix[0])
        res = -math.inf
        for ub in range(m):
            row = [0, ]*n
            for lb in range(ub, m):
                row = [(row[i]+v) for i, v in enumerate(matrix[lb])]
                res = max(res, max_sum_1d(row))
                if res == k:
                    return k
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[1, 0, 1], [0, -2, 3]]
        k = 2
        expected = 2
        self.assertEqual(sol.maxSumSubmatrix(matrix, k), expected)

    def test_case_2(self):
        sol = Solution()
        matrix = [[2, 2, -1]]
        k = 3
        expected = 3
        self.assertEqual(sol.maxSumSubmatrix(matrix, k), expected)

    def test_case_3(self):
        sol = Solution()
        matrix = [[2, 2, -1]]
        k = 0
        expected = -1
        self.assertEqual(sol.maxSumSubmatrix(matrix, k), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
