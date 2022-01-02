import unittest
from typing import List
from pprint import pprint


class Solution1:
    def lastRemaining(self, n: int, m: int) -> int:
        if n == 1:
            return 0

        return (self.lastRemaining(n-1, m)+m) % n


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2, n+1):
            res = (res + m) % i
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 5
        m = 3
        expected = 3
        self.assertEqual(sol.lastRemaining(n, m), expected)

    def test_case_2(self):
        sol = Solution()
        n = 10
        m = 17
        expected = 2
        self.assertEqual(sol.lastRemaining(n, m), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
