import unittest
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n, max_ = len(matrix), len(matrix[0]), 0
        dp = [0,]*(n+1)
        for i in range(1, m+1):
            new_dp = [0,]*(n+1)
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "0":
                    new_dp[j] = 0
                else:
                    new_dp[j] = 1 + min(dp[j-1], dp[j], new_dp[j-1])
                max_ = max(max_, new_dp[j])
            dp = new_dp
        return max_**2

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        expected = 4
        self.assertEqual(sol.maximalSquare(matrix), expected)

    def test_case_2(self):
        sol = Solution()
        matrix = [["0","1"],["1","0"]]
        expected = 1
        self.assertEqual(sol.maximalSquare(matrix), expected)

    def test_case_3(self):
        sol = Solution()
        matrix = [["0"]]
        expected = 0
        self.assertEqual(sol.maximalSquare(matrix), expected)

    # def test_edge_case_1(self):
    #     pass



if __name__ == "__main__":
    unittest.main()
