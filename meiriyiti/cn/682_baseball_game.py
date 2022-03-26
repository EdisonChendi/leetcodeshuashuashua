import unittest
from typing import List
from pprint import pprint


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for op in ops:
            if op == 'C':
                scores.pop()
            elif op == 'D':
                scores.append(2*scores[-1])
            elif op == '+':
                scores.append(scores[-2]+scores[-1])
            else:
                scores.append(int(op))
        return sum(scores)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        expected = 27
        self.assertEqual(sol.calPoints(ops), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
