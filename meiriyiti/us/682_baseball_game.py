import unittest
from typing import List
from pprint import pprint


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        board = []
        for op in ops:
            if op == 'D':
                board.append(2*board[-1])
            elif op == 'C':
                board.pop()
            elif op == '+':
                board.append(board[-1]+board[-2])
            else:
                board.append(int(op))
        return sum(board)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        ops = ["5", "2", "C", "D", "+"]
        expected = 30
        self.assertEqual(sol.calPoints(ops), expected)

    def test_case_2(self):
        sol = Solution()
        ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        expected = 27
        self.assertEqual(sol.calPoints(ops), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
