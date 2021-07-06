import unittest
from typing import List
from pprint import pprint

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1,]*n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        m = 3
        n = 7
        expected = 28
        self.assertEqual(sol.uniquePaths(m, n), expected)

    def test_case_2(self):
        sol = Solution()
        m = 3
        n = 2
        expected = 3
        self.assertEqual(sol.uniquePaths(m, n), expected)

    def test_case_3(self):
        sol = Solution()
        m = 7
        n = 3
        expected = 28
        self.assertEqual(sol.uniquePaths(m, n), expected)

    def test_case_4(self):
        sol = Solution()
        m = 3
        n = 3
        expected = 6
        self.assertEqual(sol.uniquePaths(m, n), expected)
        
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
