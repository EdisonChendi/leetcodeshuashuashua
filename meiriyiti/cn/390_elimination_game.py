import unittest
from typing import List
from pprint import pprint

class Solution:
    def lastRemaining(self, n: int) -> int:
        res = 1
        step = 1
        remain = n
        flag = True
        while remain > 1:
            if flag or remain % 2 == 1:
                res += step
            remain //= 2
            step *= 2
            flag = not flag
        return res
        

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 100
        expected =  54
        self.assertEqual(sol.lastRemaining(n), expected)


    #def test_case_3(self):
    #   sol = Solution()
    #   n = 102
    #   expected =  56
    #   self.assertEqual(sol.lastRemaining(n), expected)

        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
