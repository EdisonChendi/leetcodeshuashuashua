import unittest
from typing import List
from pprint import pprint


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = {1: [0]*n, 2: [0]*n}
        self.col = {1: [0]*n, 2: [0]*n}
        self.pie = {1: 0, 2: 0}
        self.na = {1: 0, 2: 0}

    def move(self, row: int, col: int, player: int) -> int:
        self.row[player][row] += 1
        self.col[player][col] += 1
        self.na[player] += int(row == col)
        self.pie[player] += int(row+col == self.n-1)

        if any(cnt == self.n for cnt in (self.row[player][row], self.col[player][col],
                                         self.na[player], self.pie[player])):
            return player
        return 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
