import unittest
from typing import List
from pprint import pprint

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRS = ((1,0),(0,1),(-1,0),(0,-1))
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if grid[r][c] != "1":
                return False
            
            grid[r][c] = "-1"
            for i,j in DIRS:
                nr, nc = r+i, c+j
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc)
            return True

        for r in range(m):
            for c in range(n):
                if dfs(r, c):
                    res += 1
        
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        expected = 1
        self.assertEqual(sol.numIslands(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"],
        ]
        expected = 3
        self.assertEqual(sol.numIslands(grid), expected)

        
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
