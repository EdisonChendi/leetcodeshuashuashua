import unittest
from typing import List
from pprint import pprint

from collections import Counter

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        row0, row1, row2 = board

        counter = Counter(row0)+Counter(row1)+Counter(row2)
        xo = counter['X'] - counter['O']
        if xo not in {0, 1}:
            return False
        o_win, x_win = 0, 0
        win_row0 = row0[0] == row0[1] == row0[2]
        o_win += win_row0 and row0[0] == "O"
        x_win += win_row0 and row0[0] == "X"

        win_row1 = row1[0] == row1[1] == row1[2]
        o_win += win_row1 and row1[0] == "O"
        x_win += win_row1 and row1[0] == "X"

        win_row2 = row2[0] == row2[1] == row2[2]
        o_win += win_row2 and row2[0] == "O"
        x_win += win_row2 and row2[0] == "X"

        win_col0 = row0[0] == row1[0] == row2[0]
        o_win += win_col0 and row0[0] == "O"
        x_win += win_col0 and row0[0] == "X"

        win_col1 = row0[1] == row1[1] == row2[1]
        o_win += win_col1 and row0[1] == "O"
        x_win += win_col1 and row0[1] == "X"

        win_col2 = row0[2] == row1[2] == row2[2]
        o_win += win_col2 and row0[2] == "O"
        x_win += win_col2 and row0[2] == "X"

        win_pie = row0[2] == row1[1] == row2[0]
        o_win += win_pie and row0[2] == "O"
        x_win += win_pie and row0[2] == "X"

        win_na = row0[0] == row1[1] == row2[2]
        o_win += win_na and row0[0] == "O"
        x_win += win_na and row0[0] == "X"

        if xo == 0:
            return not x_win >= 1
        
        if xo == 1:
            return not o_win >= 1

        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = ["O  ","   ","   "]
        expected = False
        self.assertEqual(sol.validTicTacToe(board), expected)

    def test_case_2(self):
        sol = Solution()
        board = ["XOX"," X ","   "]
        expected = False
        self.assertEqual(sol.validTicTacToe(board), expected)

    def test_case_3(self):
        sol = Solution()
        board = ["XXX","   ","OOO"]
        expected = False
        self.assertEqual(sol.validTicTacToe(board), expected)
        
    def test_case_4(self):
        sol = Solution()
        board = ["XOX","O O","XOX"]
        expected = True
        self.assertEqual(sol.validTicTacToe(board), expected)

    def test_case_5(self):
        sol = Solution()
        board = ["XXX","OOX","OOX"]
        expected = True
        self.assertEqual(sol.validTicTacToe(board), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
