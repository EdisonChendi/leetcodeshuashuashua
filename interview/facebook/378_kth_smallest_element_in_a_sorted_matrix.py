import unittest
from typing import List
from pprint import pprint

import heapq


class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # time: O(klgk)
        # space: O(k)
        H, W = len(matrix), len(matrix[0])
        h = [(matrix[0][0], 0, 0)]
        visited = {(0, 0)}
        v = 0
        for _ in range(k):
            v, i, j = heapq.heappop(h)
            for ni, nj in ((i+1, j), (i, j+1)):
                if 0 <= ni < H and 0 <= nj < W:
                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        heapq.heappush(h, (matrix[ni][nj], ni, nj))
        return v


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # time: O(N+Nlgk)
        # space: O(N)
        N = len(matrix)
        h = [(matrix[i][0], i, 0) for i in range(N)]
        heapq.heapify(h)
        for _ in range(k-1):
            _, i, j = heapq.heappop(h)
            j += 1
            if j < N:
                heapq.heappush(h, (matrix[i][j], i, j))
        return heapq.heappop(h)[0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        k = 8
        expected = 13
        self.assertEqual(sol.kthSmallest(matrix, k), expected)

    def test_case_2(self):
        sol = Solution()
        matrix = [[-5]]
        k = 1
        expected = -5
        self.assertEqual(sol.kthSmallest(matrix, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
