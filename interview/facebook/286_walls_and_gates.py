import unittest
from typing import List
from pprint import pprint


class Solution1:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def bfs(i, j):
            visited = {(i, j)}
            q = [(i, j, 0)]
            while q:
                next_q = []
                while q:
                    i, j, d = q.pop()
                    if d > 0 and d >= rooms[i][j]:
                        continue
                    rooms[i][j] = d
                    for di, dj in DIRs:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < H and 0 <= nj < W and rooms[ni][nj] != -1 and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            next_q.append((ni, nj, d+1))
                q = next_q

        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        H, W = len(rooms), len(rooms[0])
        for i in range(H):
            for j in range(W):
                if rooms[i][j] == 0:
                    bfs(i, j)
        return rooms


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        # 多源bfs
        DIRs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        q = []
        H, W = len(rooms), len(rooms[0])
        for i in range(H):
            for j in range(W):
                if rooms[i][j] == 0:
                    q.append((i, j))

        dist = 0
        while q:
            nxt_q = []
            while q:
                i, j = q.pop()
                if dist > 0 and dist >= rooms[i][j]:
                    continue
                rooms[i][j] = dist
                for di, dj in DIRs:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < H and 0 <= nj < W and rooms[ni][nj] != -1:
                        nxt_q.append((ni, nj))
            dist += 1
            q = nxt_q
        return rooms


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
                 [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
        expected = [[3, -1, 0, 1], [2, 2, 1, -1],
                    [1, -1, 2, -1], [0, -1, 3, 4]]
        self.assertCountEqual(sol.wallsAndGates(rooms), expected)

    def test_case_2(self):
        sol = Solution()
        rooms = [[-1]]
        expected = [[-1]]
        self.assertCountEqual(sol.wallsAndGates(rooms), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
