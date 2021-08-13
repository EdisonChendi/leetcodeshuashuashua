import unittest
from typing import List
from pprint import pprint

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        borders = (zip([0,]*n, range(n)),
                   zip([m-1,]*n, range(n)),
                   zip(range(m), [0,]*m),
                   zip(range(m), [n-1,]*m))

        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "Y"
                for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    dfs(ni,nj)

        for b in borders:
            for i, j in b:
                dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O": board[i][j] = "X"
                if board[i][j] == "Y": board[i][j] = "O"


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        sol.solve(board)
        expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        self.assertCountEqual(board, expected)

    def test_case_2(self):
        sol = Solution()
        board = [["X"]] 
        sol.solve(board)
        expected = [["X"]]
        self.assertCountEqual(board, expected)

        
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
