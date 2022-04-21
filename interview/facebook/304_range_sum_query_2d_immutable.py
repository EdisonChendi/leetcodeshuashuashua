import unittest
from typing import List
from pprint import pprint


class NumMatrix1:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = self._gen_prefix()

    def _gen_prefix(self):
        res = []
        for row in self.matrix:
            cur = [0]
            for v in row:
                cur.append(cur[-1]+v)
            res.append(cur)
        return res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2+1):
            prefix = self.prefix[r]
            res += prefix[col2+1] - prefix[col1]
        return res


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.H, self.W = len(self.matrix), len(self.matrix[0])
        self.prefix = self._gen_square_prefix()

    def _gen_square_prefix(self):
        dp = [[0]*self.W for _ in range(self.H)]
        dp[0] = self.matrix[0][:]
        for i in range(1, self.W):
            dp[0][i] = self.matrix[0][i] + dp[0][i-1]
        for i in range(1, self.H):
            dp[i][0] = dp[i-1][0] + self.matrix[i][0]
            for j in range(1, self.W):
                dp[i][j] = self.matrix[i][j] + \
                    dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        return dp

    def get_prefix(self, r, c):
        if r < 0 or c < 0:
            return 0
        return self.prefix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.get_prefix(row2, col2) - self.get_prefix(row1-1, col2) - self.get_prefix(row2, col1-1) + self.get_prefix(row1-1, col1-1)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
