import unittest
from typing import List
from pprint import pprint

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.strip().split())

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "Hello, my name is John"
        expected = 5
        self.assertEqual(sol.countSegments(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "Hello"
        expected = 1
        self.assertEqual(sol.countSegments(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "love live! mu'sic forever"
        expected = 4
        self.assertEqual(sol.countSegments(s), expected)
        
    def test_case_4(self):
        sol = Solution()
        s = ""
        expected = 0
        self.assertEqual(sol.countSegments(s), expected)
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
