import unittest
from typing import List
from pprint import pprint

import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = [math.inf]

    def __len__(self):
        return len(self.stack)

    def __bool__(self):
        return bool(self.stack)

    def push(self, val: int) -> None:
        self.mins.append(min(val, self.mins[-1]))
        self.stack.append(val)

    def pop(self) -> None:
        if not self:
            raise ""
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        if not self:
            raise ""
        return self.stack[-1]

    def getMin(self) -> int:
        if not self:
            raise ""
        return self.mins[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        self.assertEqual(obj.getMin(), -3)
        param_3 = obj.top()
        self.assertEqual(param_3, -3)
        obj.pop()
        self.assertEqual(obj.getMin(), -2)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
