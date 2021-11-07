import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x, y = m, n
        for a, b in ops:
            x = min(x, a)
            y = min(y, b)
        return x*y


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        m = 3
        n = 3
        ops = [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3],
               [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]
        expected = 4
        self.assertEqual(sol.maxCount(m, n, ops), expected)

    def test_case_2(self):
        sol = Solution()
        m = 3
        n = 3
        ops = []
        expected = 9
        self.assertEqual(sol.maxCount(m, n, ops), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
