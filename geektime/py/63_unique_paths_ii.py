import unittest
from typing import List
from pprint import pprint


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0, 1] + [0, ]*(n-1)
        for i in range(m):
            for j in range(1, n+1):
                if obstacleGrid[i][j-1] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j-1]
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = 2
        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), expected)

    def test_case_2(self):
        sol = Solution()
        obstacleGrid = [[0, 1], [0, 0]]
        expected = 1
        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), expected)

    def test_case_3(self):
        sol = Solution()
        obstacleGrid = [[0]]
        expected = 1
        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), expected)

    def test_case_4(self):
        sol = Solution()
        obstacleGrid = [[1]]
        expected = 0
        self.assertEqual(sol.uniquePathsWithObstacles(obstacleGrid), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
