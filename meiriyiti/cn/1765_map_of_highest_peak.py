import unittest
from typing import List
from pprint import pprint


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        H, W = len(isWater), len(isWater[0])
        water = set()
        res = [[H+W]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if isWater[i][j] == 1:
                    water.add((i, j))
                    res[i][j] = 0

        q = water
        step = 1
        while q:
            nxt_q = set()
            while q:
                i, j = q.pop()
                for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= ni < H and 0 <= nj < W and res[ni][nj] > step:
                        res[ni][nj] = step
                        nxt_q.add((ni, nj))
            step += 1
            q = nxt_q

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        isWater = [[0, 1], [0, 0]]
        expected = [[1, 0], [2, 1]]
        self.assertEqual(sol.highestPeak(isWater), expected)

    def test_case_2(self):
        sol = Solution()
        isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
        expected = [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
        self.assertEqual(sol.highestPeak(isWater), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
