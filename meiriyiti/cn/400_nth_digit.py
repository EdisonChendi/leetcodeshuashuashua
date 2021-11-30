import unittest
from typing import List
from pprint import pprint

"""
1*9 - 1-9
2*90 - 10-99
3*900 - 100-999
4*9000 - 1000-9999
5*90000 - 
6*900000 - 
7*9
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        acc, i = 0, 0
        while True:
            nxt = (i+1)*9*(10**i)
            if acc+nxt > n:
                break
            i += 1
            acc += nxt
        cnt, rem = divmod(n-acc, i+1)
        num = 10**i+cnt-1
        if rem == 0:
            return num % 10
        else:
            return (num+1)//(10**(i+1-rem)) % 10


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        expected = 3
        self.assertEqual(sol.findNthDigit(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 11
        expected = 0
        self.assertEqual(sol.findNthDigit(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
