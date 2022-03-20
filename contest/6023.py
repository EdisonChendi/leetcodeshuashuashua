import unittest
from typing import List
from pprint import pprint


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        N = len(floor)
        dp = [0]*(N+1)

        white_presums = [0]
        for f in floor:
            white_presums.append(white_presums[-1]+(f == '1'))

        for _ in range(numCarpets):
            new_dp = [0]*(N+1)
            for i in range(1, N+1):
                if i-carpetLen >= 0:
                    add_one = dp[i-carpetLen] + \
                        white_presums[i] - white_presums[i-carpetLen]
                else:
                    add_one = white_presums[i]
                new_dp[i] = max(new_dp[i-1], add_one)
            dp = new_dp

        return white_presums[-1] - dp[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        floor = "10110101"
        numCarpets = 2
        carpetLen = 2
        expected = 2
        self.assertEqual(sol.minimumWhiteTiles(
            floor, numCarpets, carpetLen), expected)

    def test_case_2(self):
        sol = Solution()
        floor = "11111"
        numCarpets = 2
        carpetLen = 3
        expected = 0
        self.assertEqual(sol.minimumWhiteTiles(
            floor, numCarpets, carpetLen), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
