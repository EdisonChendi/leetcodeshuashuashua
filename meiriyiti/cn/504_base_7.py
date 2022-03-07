import unittest
from typing import List
from pprint import pprint


class Solution:
    def convertToBase7(self, num: int) -> str:
        n = abs(num)
        if n == 0:
            return '0'
        res = []
        while n > 0:
            res.append(str(n%7))
            n //= 7
        if num < 0:
            res.append('-') 
        return "".join(reversed(res))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = 100
        expected = "202"
        self.assertEqual(sol.convertToBase7(num), expected)

    def test_case_2(self):
        sol = Solution()
        num = -7
        expected = "-10"
        self.assertEqual(sol.convertToBase7(num), expected)
        
    def test_edge_case_1(self):
        sol = Solution()
        num = 0
        expected = "0"
        self.assertEqual(sol.convertToBase7(num), expected)
        


if __name__ == "__main__":
    unittest.main()
