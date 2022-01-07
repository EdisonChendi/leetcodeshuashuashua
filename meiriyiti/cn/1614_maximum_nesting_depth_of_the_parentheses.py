import unittest
from typing import List
from pprint import pprint

class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        opens = 0
        for ch in s:
            if ch == '(':
                opens += 1
            elif ch == ')':
                res = max(res, opens)
                opens -= 1
        return res

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "(1+(2*3)+((8)/4))+1"
        expected = 3
        self.assertEqual(sol.maxDepth(s), expected)
        
    def test_case_2(self):
        sol = Solution()
        s = "(1)+((2))+(((3)))"
        expected = 3
        self.assertEqual(sol.maxDepth(s), expected)
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
