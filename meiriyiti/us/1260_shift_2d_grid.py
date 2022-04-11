import unittest
from typing import List
from pprint import pprint


class Solution1:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # naive approach
        def get_col(i):
            return [row[i] for row in grid]

        def shift(grid):
            last = get_col(0)
            for i in range(1, W):
                cur = get_col(i)
                for j in range(H):
                    grid[j][i] = last[j]
                last = cur

            grid[0][0] = last[-1]
            for i in range(1, H):
                grid[i][0] = last[i-1]

        H, W = len(grid), len(grid[0])
        for _ in range(k):
            shift(grid)
        return grid


class Solution2:
    # time complexity - O(size of matrix)
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        H, W = len(grid), len(grid[0])
        res = [[0]*W for _ in range(H)]
        for c in range(W):
            rotate, move = divmod(c+k, W)
            for i, n in enumerate(row[c] for row in grid):
                res[(i+rotate) % H][move] = n
        return res


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        H, W = len(grid), len(grid[0])
        for _ in range(k):
            prev = grid[-1][-1]
            for r in range(H):
                for c in range(W):
                    grid[r][c], prev = prev, grid[r][c]
        return grid


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 1
        expected = [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.assertCountEqual(sol.shiftGrid(grid, k), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
        k = 4
        expected = [[12, 0, 21, 13], [3, 8, 1, 9],
                    [19, 7, 2, 5], [4, 6, 11, 10]]
        self.assertCountEqual(sol.shiftGrid(grid, k), expected)

    def test_case_3(self):
        sol = Solution()
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 9
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertCountEqual(sol.shiftGrid(grid, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
