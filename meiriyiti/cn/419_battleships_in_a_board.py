import unittest
from typing import List
from pprint import pprint


class Solution1:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        H, W = len(board), len(board[0])
        for i in range(H):
            for j in range(W):
                cell = board[i][j]
                if cell == ".":
                    continue
                board[i][j] = "."
                for k in range(j+1, W):
                    if board[i][k] != "X":
                        break
                    board[i][k] = "."
                for k in range(i+1, H):
                    if board[k][j] != "X":
                        break
                    board[k][j] = "."
                res += 1
        return res


class Solution2:
    def countBattleships(self, board: List[List[str]]) -> int:
        def is_upleft(i, j):
            return not ((i > 0 and board[i-1][j] == "X") or (j > 0 and board[i][j-1] == "X"))

        res = 0
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == "X" and is_upleft(i, j):
                    res += 1
        return res


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue
                if i > 0 and board[i-1][j] == "X":
                    continue
                if j > 0 and board[i][j-1] == "X":
                    continue
                res += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [["X", ".", ".", "X"], [
            ".", ".", ".", "X"], [".", ".", ".", "X"]]
        expected = 2
        self.assertEqual(sol.countBattleships(board), expected)

    def test_case_2(self):
        sol = Solution()
        board = [["."]]
        expected = 0
        self.assertEqual(sol.countBattleships(board), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
