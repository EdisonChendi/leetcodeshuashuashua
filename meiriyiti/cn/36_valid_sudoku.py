import unittest
from typing import List
from pprint import pprint


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        b = [set() for _ in range(9)]
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue
                if num in r[i] or num in c[j] or num in b[i//3*3+j//3]:
                    return False
                r[i].add(num)
                c[j].add(num)
                b[i//3*3+j//3].add(num)
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
        self.assertTrue(sol.isValidSudoku(board))

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
