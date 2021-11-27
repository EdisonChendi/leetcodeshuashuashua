from math import exp
import unittest
from typing import List
from pprint import pprint
import traceback
import random


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.reset()

    def flip(self) -> List[int]:
        x = random.randrange(0, self.total)
        n = self.map.get(x, x)
        self.total -= 1
        self.map[x] = self.map.get(self.total, self.total)
        return [n//self.n, n % self.n]

    def reset(self) -> None:
        self.total = self.m*self.n
        self.map = {}


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        try:
            m, n = 1, 10
            sol = Solution(m, n)
            res = []
            for _ in range(m*n):
                res.append(sol.flip())
            for row in sorted(res):
                print(row)
        except Exception as e:
            traceback.print_exc()
            print("Error!")
            print(sol.row_end)
            print(sol.col_end)
            print(sol.row)
            print(sol.col)
        # print(sol.reset())
        # print(sol.flip())
        # print(sol.flip())
        # print(sol.flip())
        # print(sol.reset())

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
