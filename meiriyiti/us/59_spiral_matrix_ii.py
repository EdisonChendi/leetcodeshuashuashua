import unittest
from typing import List
from pprint import pprint

class Solution1:
    def generateMatrix(self, n: int) -> List[List[int]]:
        DIRs = ((0,1),(1,0),(0,-1),(-1,0))
        cur = 0
        cnt = 0
        res = [[0]*n for _ in range(n)]
        i,j = 0,-1
        while cnt < n*n:
            di, dj = DIRs[cur%4]
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and res[ni][nj]==0:
                i,j = ni,nj
                res[i][j] = cnt+1
                cnt += 1
            else:
                cur += 1
        return res

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        i,j = 0,0
        di, dj = 0, 1
        v = 0
        while v < n*n:
            res[i][j] = v+1
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and res[ni][nj] == 0:
                i, j = ni, nj
            else:
                di, dj = dj, -di
                i, j = i+di, j+dj
            v += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        expected = [[1,2,3],[8,9,4],[7,6,5]]
        self.assertCountEqual(sol.generateMatrix(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        expected = [[1]]
        self.assertCountEqual(sol.generateMatrix(n), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
