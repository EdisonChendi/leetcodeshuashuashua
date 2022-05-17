import unittest
from typing import List
from pprint import pprint

import math
import heapq

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        # run bfs for fire
        def fire_fire(fires):
            res = [[math.inf] * W for _ in range(H)]
            q = fires
            time = 0
            while q:
                nxt_q = []
                for i,j in q:
                    res[i][j] = time
                    for di, dj in DIRs:
                        ni, nj = i+di, j+dj
                        if 0 <= ni< H and 0 <= nj < W \
                            and grid[ni][nj] != 2 \
                            and res[ni][nj] == math.inf:
                            nxt_q.append((ni,nj))
                q = nxt_q
                time += 1
            return res
        
        DIRs = ((0,1),(0,-1),(1,0),(-1,0))
        H,W = len(grid), len(grid[0])
        fires = [(i,j) for i, row in enumerate(grid) for j, n in enumerate(row) if n == 1]
        f = fire_fire(fires)

        q = [(-math.inf, 0, 0, 0)]
        visited = {(0,0): math.inf}
        res = -math.inf
        while q:
            wait,i,j,t = heapq.heappop(q)
            wait = -wait
            if (i,j) == (H-1,W-1):
                wait = min(wait, f[i][j]-t)
                res = max(res, wait)
                return res if res < math.inf else 10**9

            if f[i][j] > t:
                wait = min(wait, f[i][j]-t-1)
                for di, dj in DIRs:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < H and 0 <= nj < W \
                        and grid[ni][nj] != 2 \
                        and ((ni,nj) not in visited or visited[(ni,nj)] < wait):
                        visited[(ni,nj)] = wait
                        heapq.heappush(q, (-wait, ni, nj, t+1))
        return -1

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [[0,0,0,0,0],[0,2,0,2,0],[0,2,0,2,0],[0,2,1,2,0],[0,2,2,2,0],[0,0,0,0,0]]
        # grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
        print(sol.maximumMinutes(grid))
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
