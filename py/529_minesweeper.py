import unittest
from typing import List
from pprint import pprint


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]
        r, c = len(board), len(board[0])
        visited = set()

        def dfs(x, y):
            # step 1 - look around first
            count = 0
            nxt = []
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c:
                    if board[nx][ny] == "M":
                        count += 1
                    else:
                        if board[nx][ny] == "E" and (nx, ny) not in visited:
                            nxt.append((nx, ny))

            # step 2
            # rule 2 - show count & stop
            if count > 0:
                board[x][y] = str(count)
            else:
                # rule 3 - go sweep deeper
                board[x][y] = "B"
                for nx, ny in nxt:
                    visited.add((nx, ny))
                    dfs(nx, ny)

        dfs(click[0], click[1])
        return board


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"],
                 ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
        click = [3, 0]
        expected = [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], [
            "B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
        res = sol.updateBoard(board, click)
        self.assertCountEqual(res, expected)

    def test_case_2(self):
        sol = Solution()
        board = [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"],
                 ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
        click = [1, 2]
        expected = [["B", "1", "E", "1", "B"], ["B", "1", "X", "1", "B"], [
            "B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
        res = sol.updateBoard(board, click)
        self.assertCountEqual(res, expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
