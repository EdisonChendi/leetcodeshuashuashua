import unittest
from typing import List
from pprint import pprint


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        accounts = [[1, 5], [7, 3], [3, 5]]
        expected = 10
        self.assertEqual(sol.maximumWealth(accounts), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
