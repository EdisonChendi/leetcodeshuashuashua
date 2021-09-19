import unittest
from typing import List
from pprint import pprint
from heapq import heappop, heappush


class Solution:
    def minSteps(self, n: int) -> int:
        # math
        # prime factorization
        # [cpp][cpppp][cppppp]
        res, N = 0, n
        p = 2
        while n > 1:
            while n % p == 0:
                n //= p
                res += p
            p = p+1
        return res

    def minSteps1(self, n: int) -> int:
        # use bfs + pruning

        if n == 1:
            return 0

        # do a copy first
        # (num, buf, last_op(0-copy, 1-paste))
        q = [(1, 1, 0), ]
        visited = set((1, 1))
        operations = 1

        while q:
            new_q = []
            while q:
                num, buf, last_op = q.pop()
                if num == n:
                    return operations
                # do copy
                if last_op == 1:
                    copy = (num, num)
                    if copy not in visited:
                        visited.add(copy)
                        new_q.append((copy[0], copy[1], 0))
                # do paste
                paste = (num+buf, buf)
                if paste not in visited and paste[0] <= n:
                    visited.add(paste)
                    new_q.append((paste[0], paste[1], 1))
            q = new_q
            operations += 1

        return operations


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        expected = 3
        self.assertEqual(sol.minSteps(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
