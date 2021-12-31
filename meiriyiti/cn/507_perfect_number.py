import unittest
from typing import List
from pprint import pprint


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return True

        s = 1
        i = 2
        while i*i < num:
            if num % i == 0:
                s += i
                s += num // i
            i += 1
        if i*i == num:
            s += i
        return s == num


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = 28
        expceted = True
        self.assertEqual(sol.checkPerfectNumber(num), expceted)

    def test_case_2(self):
        sol = Solution()
        num = 7
        expceted = False
        self.assertEqual(sol.checkPerfectNumber(num), expceted)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
