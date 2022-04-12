import unittest
from typing import List
from pprint import pprint


class Solution1:
    # O(H*W) space
    def gameOfLife(self, board: List[List[int]]) -> None:
        def get(i, j):
            if 0 <= i < H and 0 <= j < W:
                return clone[i][j]
            return 0

        def change(i, j):

            live_neibors = sum(get(i+ni, j+nj) for ni, nj in DIRs)
            if get(i, j) == 0:
                return live_neibors == 3
            else:
                return live_neibors == 2 or live_neibors == 3

        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1))
        H, W = len(board), len(board[0])
        clone = [row[:] for row in board]
        for i in range(H):
            for j in range(W):
                board[i][j] = int(change(i, j))


class Solution:
    # O(H*W) space
    def gameOfLife(self, board: List[List[int]]) -> None:
        def get(i, j):
            if 0 <= i < H and 0 <= j < W and board[i][j] in {1, -1}:
                return 1
            return 0

        def change(i, j):
            live_neibors = sum(get(i+ni, j+nj) for ni, nj in DIRs)
            if get(i, j) == 0:
                # 2: 0 -> 1
                return 2 if live_neibors == 3 else 0
            else:
                # -1: 1 -> 0
                return -1 if live_neibors < 2 or live_neibors > 3 else 1

        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1))
        H, W = len(board), len(board[0])
        for i in range(H):
            for j in range(W):
                board[i][j] = int(change(i, j))

        for i in range(H):
            for j in range(W):
                board[i][j] = int(board[i][j] > 0)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        sol.gameOfLife(board)
        self.assertCountEqual(board, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
