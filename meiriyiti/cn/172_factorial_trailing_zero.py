import unittest
from typing import List
from pprint import pprint


class Solution:
    def trailingZeroes(self, n: int) -> int:
        div = 5
        ans = 0
        while div <= n:
            ans += n // div
            div *= 5
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 5
        expected = 1
        self.assertEqual(sol.trailingZeroes(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
