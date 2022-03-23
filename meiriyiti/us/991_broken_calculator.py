from hashlib import new
import unittest
from typing import List
from pprint import pprint

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        step = 0
        while target > startValue:
            if target & 1 == 1:
                target += 1
            else:
                target //= 2
            step += 1
        return step + startValue - target


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        startValue = 2
        target = 3
        expected = 2
        self.assertEqual(sol.brokenCalc(startValue, target), expected)
        
    def test_case_2(self):
        sol = Solution()
        startValue = 5
        target = 8
        expected = 2
        self.assertEqual(sol.brokenCalc(startValue, target), expected)

    def test_case_3(self):
        sol = Solution()
        startValue = 3
        target = 10
        expected = 3
        self.assertEqual(sol.brokenCalc(startValue, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
