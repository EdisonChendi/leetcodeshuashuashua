import unittest
from typing import List
from pprint import pprint


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        h, w = len(matrix), len(matrix[0])

        # col prefix sum
        col_prefix_sum = [[0, ]*w for _ in range(h+1)]
        for i in range(1, h+1):
            for j in range(w):
                col_prefix_sum[i][j] = col_prefix_sum[i-1][j] + matrix[i-1][j]

        res, ma = [0, 0, 0, 0], matrix[0][0]
        for i in range(1, h+1):
            for j in range(i, h+1):
                cur_max = col_prefix_sum[j][0] - col_prefix_sum[i-1][0]
                col_begin = 0
                for k in range(1, w):
                    col_sum = col_prefix_sum[j][k] - col_prefix_sum[i-1][k]
                    if cur_max < 0:
                        cur_max = col_sum
                        col_begin = k
                    else:
                        cur_max += col_sum

                    if cur_max > ma:
                        ma = cur_max
                        res = [i-1, col_begin, j-1, k]
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[-1, 0], [0, -1]]
        expected = [0, 1, 0, 1]
        self.assertListEqual(sol.getMaxMatrix(matrix), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
