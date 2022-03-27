import unittest
from typing import List
from pprint import pprint


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        H, W = len(mat), len(mat[0])
        res = []
        for c in range(W+1):
            for r in range(H):
                if (c == 0 or mat[r][c-1] == 1) and (c == W or mat[r][c] == 0):
                    res.append(r)
                    k -= 1
                    if k == 0:
                        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        mat = [[1, 1, 0, 0, 0],
               [1, 1, 1, 1, 0],
               [1, 0, 0, 0, 0],
               [1, 1, 0, 0, 0],
               [1, 1, 1, 1, 1]]
        k = 3
        expected = [2, 0, 3]
        self.assertListEqual(sol.kWeakestRows(mat, k), expected)

    def test_case_2(self):
        sol = Solution()
        mat = [[1, 0, 0, 0],
               [1, 1, 1, 1],
               [1, 0, 0, 0],
               [1, 0, 0, 0]]
        k = 2
        expected = [0, 2]
        self.assertListEqual(sol.kWeakestRows(mat, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
