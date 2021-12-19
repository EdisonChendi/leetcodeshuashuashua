import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        # dp[i][j]
        # i - end of the slice array
        # j - the number of the pieces chosen
        # dp[i][j] = max(dp[i-1][j], dp[i-2][j-1]+slice[i])
        def sub(slices: List[int]) -> int:
            N = len(slices)
            choose = N // 3 + int(N % 3 > 0)
            dp = [[0]*(choose+1) for _ in range(N+1)]
            for i in range(1, N+1):
                for j in range(1, choose+1):
                    dp[i][j] = max(dp[i-1][j],
                                   slices[i-1] + (dp[i-2][j-1] if i >= 2 else 0))
            return dp[-1][-1]

        return max(sub(slices[:-1]), sub(slices[1:]))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        slices = [1, 2, 3, 4, 5, 6]
        expected = 10
        self.assertEqual(sol.maxSizeSlices(slices), expected)

    def test_case_2(self):
        sol = Solution()
        slices = [8, 9, 8, 6, 1, 1]
        expected = 16
        self.assertEqual(sol.maxSizeSlices(slices), expected)

    def test_case_3(self):
        sol = Solution()
        slices = [4, 1, 2, 5, 8, 3, 1, 9, 7]
        expected = 21
        self.assertEqual(sol.maxSizeSlices(slices), expected)

    def test_case_4(self):
        sol = Solution()
        slices = [3, 1, 2]
        expected = 3
        self.assertEqual(sol.maxSizeSlices(slices), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
