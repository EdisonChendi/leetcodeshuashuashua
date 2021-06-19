import unittest
from typing import List
from pprint import pprint


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f1, f2 = 1, 2
        for _ in range(2, n):
            f1, f2 = f2, f1+f2
        return f2


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 2
        expected = 2
        self.assertEqual(sol.climbStairs(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 3
        expected = 3
        self.assertEqual(sol.climbStairs(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 4
        expected = 5
        self.assertEqual(sol.climbStairs(n), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
