import unittest
from typing import List
from pprint import pprint
from collections import defaultdict, Counter


class DetectSquares:

    def __init__(self):
        self.y = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.y[y][x] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point
        if py not in self.y:
            return 0
        py_xcnt = self.y[py]
        for y, y_xcnt in self.y.items():
            if y == py:
                continue
            d = y-py
            ans += y_xcnt[px] * py_xcnt[px+d] * y_xcnt[px+d]
            ans += y_xcnt[px] * py_xcnt[px-d] * y_xcnt[px-d]

        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        ds = DetectSquares()
        ds.add([3, 10])
        ds.add([11, 2])
        ds.add([3, 2])
        print(ds.count([11, 10]))
        print(ds.count([14, 8]))
        ds.add([11, 2])
        print(ds.count([11, 10]))

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
