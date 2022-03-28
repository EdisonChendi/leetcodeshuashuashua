import unittest
from typing import List
from pprint import pprint

class Solution1:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n>>1)
        return a & (a+1) == 0

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 2
        while n:
            n, cur = divmod(n,2)
            if cur == prev:
                return False
            prev = cur
        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 5
        expected = True
        self.assertEqual(sol.hasAlternatingBits(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 7
        expected = False
        self.assertEqual(sol.hasAlternatingBits(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 11
        expected = False
        self.assertEqual(sol.hasAlternatingBits(n), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
