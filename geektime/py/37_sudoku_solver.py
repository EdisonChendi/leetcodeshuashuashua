import unittest
from typing import List
from pprint import pprint


def possible_values(board):
    rows, cols, blocks = [set(map(str, range(1, 10))) for _ in range(9)], [set(map(
        str, range(1, 10))) for _ in range(9)], [set(map(str, range(1, 10))) for _ in range(9)]
    for i in range(81):
        r, c = divmod(i, 9)
        b = 3*(r//3) + c//3
        n = board[r][c]
        if n == ".":
            continue
        rows[r].remove(n)
        cols[c].remove(n)
        blocks[b].remove(n)
    return rows, cols, blocks


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, blocks = possible_values(board)

        def backtrack(i):
            if i == 81:
                return True
            r, c = divmod(i, 9)
            b = 3*(r//3) + c//3
            if board[r][c] != ".":
                return backtrack(i+1)
            for n in rows[r] & cols[c] & blocks[b]:
                board[r][c] = n
                rows[r].remove(n)
                cols[c].remove(n)
                blocks[b].remove(n)
                if backtrack(i+1):
                    return True
                board[r][c] = "."
                rows[r].add(n)
                cols[c].add(n)
                blocks[b].add(n)

            return False

        backtrack(0)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                              ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        expected = [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], [
            "4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
        sol.solveSudoku(board)
        self.assertCountEqual(board, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
