import unittest
from typing import List
from pprint import pprint

import bisect

MOD = 10**9 + 7


class Fancy1:

    def __init__(self):
        self.arr = []
        self.ops = []

    def append(self, val: int) -> None:
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        if not self.arr:
            return
        self.ops.append((len(self.arr)-1, 0, inc))

    def multAll(self, m: int) -> None:
        if not self.arr:
            return
        self.ops.append((len(self.arr)-1, 1, m))

    def getIndex(self, idx: int) -> int:
        # LTE
        if idx >= len(self.arr):
            return -1
        op_idx = bisect.bisect_left(self.ops, (idx, 0, 0))
        ans = self.arr[idx]
        for i in range(op_idx, len(self.ops)):
            _, op, v = self.ops[i]
            if op == 0:
                ans = (ans + v) % MOD
            else:
                ans = (ans * v) % MOD
        return ans


class Fancy:

    def __init__(self):
        pass

    def append(self, val: int) -> None:
        pass

    def addAll(self, inc: int) -> None:
        pass

    def multAll(self, m: int) -> None:
        pass

    def getIndex(self, idx: int) -> int:
        pass


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        fancy = Fancy()

        fancy.append(2)  # fancy sequence: [2]
        fancy.addAll(3)  # fancy sequence: [2+3] -> [5]
        fancy.append(7)  # fancy sequence: [5, 7]
        fancy.multAll(2)  # fancy sequence: [5*2, 7*2] -> [10, 14]
        print(fancy.getIndex(0))  # return 10
        fancy.addAll(3)  # fancy sequence: [10+3, 14+3] -> [13, 17]
        fancy.append(10)  # fancy sequence: [13, 17, 10]
        fancy.multAll(2)  # fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
        print(fancy.getIndex(0))  # return 26
        print(fancy.getIndex(1))  # return 34
        print(fancy.getIndex(2))  # return 20

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
