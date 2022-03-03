import unittest
from typing import List
from pprint import pprint

class Solution1:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            next_num = 0
            while num > 0:
                next_num += num%10
                num //= 10
            num = next_num
        return num

class Solution:
    def addDigits(self, num: int) -> int:
        if num > 9:
            num = num % 9
            if num == 0:
                num = 9
        return num

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = 38
        expected = 2
        self.assertEqual(sol.addDigits(num), expected)

    def test_case_2(self):
        sol = Solution()
        num = 3899
        expected = 2
        self.assertEqual(sol.addDigits(num), expected)
        
    def test_case_3(self):
        sol = Solution()
        num = 0
        expected = 0
        self.assertEqual(sol.addDigits(num), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
