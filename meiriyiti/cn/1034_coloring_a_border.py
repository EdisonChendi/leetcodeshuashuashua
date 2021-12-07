import unittest
from typing import List
from pprint import pprint


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def on_grid_border(r, c):
            return r == 0 or r == H-1 or c == 0 or c == W-1

        def inside(r, c):
            return 0 <= r < H and 0 <= c < W

        H, W = len(grid), len(grid[0])
        visited = [[False]*W for _ in range(H)]
        q = [(row, col)]
        clr = grid[row][col]
        borders = []

        while q:
            nxt_q = []
            while q:
                r, c = q.pop()
                if on_grid_border(r, c):
                    borders.append((r, c))
                for nr, nc in ((r, c+1), (r, c-1), (r-1, c), (r+1, c)):
                    if inside(nr, nc):
                        if grid[nr][nc] != clr:
                            borders.append((r, c))
                        elif not visited[nr][nc]:
                            visited[nr][nc] = True
                            nxt_q.append((nr, nc))
            q = nxt_q
        for r, c in borders:
            grid[r][c] = color
        return grid


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[1, 1], [1, 2]]
        row = 0
        col = 0
        color = 3
        expected = [[3, 3], [3, 2]]
        self.assertCountEqual(sol.colorBorder(grid, row, col, color), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[1, 2, 2], [2, 3, 2]]
        row = 0
        col = 1
        color = 3
        expected = [[1, 3, 3], [2, 3, 3]]
        self.assertCountEqual(sol.colorBorder(grid, row, col, color), expected)

    def test_case_3(self):
        sol = Solution()
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        row = 1
        col = 1
        color = 2
        expected = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
        self.assertCountEqual(sol.colorBorder(grid, row, col, color), expected)

    def test_case_4(self):
        sol = Solution()
        grid = [[1, 2, 1, 2, 1, 2], [2, 2, 2, 2, 1, 2], [1, 2, 2, 2, 1, 2]]
        row = 1
        col = 3
        color = 1
        expected = [[1, 1, 1, 1, 1, 2], [1, 2, 1, 1, 1, 2], [1, 1, 1, 1, 1, 2]]
        self.assertCountEqual(sol.colorBorder(grid, row, col, color), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
