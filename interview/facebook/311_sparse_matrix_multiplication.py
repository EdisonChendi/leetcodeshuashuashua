import unittest
from typing import List
from pprint import pprint


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        def sparse_matrix(mat):
            return [{i: n for i, n in enumerate(row) if n} for row in mat]

        rows = sparse_matrix(mat1)
        cols = sparse_matrix(zip(*mat2))

        res = []
        for row in rows:
            cur = []
            for col in cols:
                nonzero = row.keys() & col.keys()
                cur.append(sum(row[i]*col[i] for i in nonzero))
            res.append(cur)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        mat1 = [[1, 0, 0], [-1, 0, 3]]
        mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
        expected = [[7, 0, 0], [-7, 0, 3]]
        self.assertCountEqual(sol.multiply(mat1, mat2), expected)

    def test_case_2(self):
        sol = Solution()
        mat1 = [[0]]
        mat2 = [[0]]
        expected = [[0]]
        self.assertCountEqual(sol.multiply(mat1, mat2), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
