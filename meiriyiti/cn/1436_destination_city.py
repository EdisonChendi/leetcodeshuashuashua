import unittest
from typing import List
from pprint import pprint


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return ({t for _, t in paths}-{f for f, _ in paths}).pop()


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        paths = [["London", "New York"], [
            "New York", "Lima"], ["Lima", "Sao Paulo"]]
        expected = "Sao Paulo"
        self.assertEqual(sol.destCity(paths), expected)

    def test_case_2(self):
        sol = Solution()
        paths = [["B", "C"], ["D", "B"], ["C", "A"]]
        expected = "A"
        self.assertEqual(sol.destCity(paths), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
