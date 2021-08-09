import unittest
from typing import List
from pprint import pprint


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        blocks = [[False, ]*(N+1) for _ in range(N)]
        rows = [[False, ]*(N+1) for _ in range(N)]
        cols = [[False, ]*(N+1) for _ in range(N)]

        for r, row in enumerate(board):
            for c, ch in enumerate(row):
                if ch == ".":
                    continue

                v = int(ch)
                block = blocks[r//3*3+c//3]
                row = rows[r]
                col = cols[c]

                if block[v] or row[v] or col[v]:
                    return False

                block[v] = True
                row[v] = True
                col[v] = True

        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        expected = True
        self.assertEqual(sol.isValidSudoku(board), expected)

    def test_case_2(self):
        sol = Solution()
        board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        expected = False
        self.assertEqual(sol.isValidSudoku(board), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
