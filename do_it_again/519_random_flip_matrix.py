import unittest
from typing import List
from pprint import pprint

import random


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.reset()

    def flip(self) -> List[int]:
        c = random.randrange(0, self.total)
        idx = self.indices.get(c, c)
        self.total -= 1
        self.indices[c] = self.indices.get(self.total, self.total)
        return [idx//self.n, idx % self.n]

    def reset(self) -> None:
        self.indices = {}
        self.total = self.m*self.n


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
