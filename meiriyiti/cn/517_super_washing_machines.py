import unittest
from typing import List
from pprint import pprint


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        N, s = len(machines), sum(machines)
        if s % N != 0:
            return -1
        avg, res, accu = s//N, 0, 0
        for m in machines:
            m -= avg
            accu += m
            res = max(res, abs(accu), m)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        machines = [1, 0, 5]
        expected = 3
        self.assertEqual(sol.findMinMoves(machines), expected)

    def test_case_2(self):
        sol = Solution()
        machines = [0, 3, 0]
        expected = 2
        self.assertEqual(sol.findMinMoves(machines), expected)

    def test_case_3(self):
        sol = Solution()
        machines = [0, 2, 0]
        expected = -1
        self.assertEqual(sol.findMinMoves(machines), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
