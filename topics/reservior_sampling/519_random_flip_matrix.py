import unittest
from typing import List
from pprint import pprint

import random


class Solution1:
    # LTE

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.reset()

    def flip(self) -> List[int]:
        chosen = -1
        cnt = 0
        for i in range(self.m*self.n):
            if self.arr[i] == 1:
                continue
            cnt += 1
            if random.randrange(0, cnt) == 0:
                chosen = i
        self.arr[chosen] = 1
        return [chosen % self.m, chosen % self.n]

    def reset(self) -> None:
        self.arr = [0]*self.m*self.n


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.reset()

    def flip(self) -> List[int]:
        pick = random.randrange(self.unflipped)
        idx = self.indices.get(pick, pick)
        self.unflipped -= 1
        self.indices[pick] = self.indices.get(self.unflipped, self.unflipped)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.indices = {}
        self.unflipped = self.m*self.n


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
