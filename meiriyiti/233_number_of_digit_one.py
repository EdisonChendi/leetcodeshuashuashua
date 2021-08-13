import unittest
from typing import List
from pprint import pprint

class Solution:
    def countDigitOne(self, n: int) -> int:
        res,base = 0,1
        while n >= base:
            res += n//(base*10)*base
            remainder = n%(base*10)
            if remainder < base:
                res += 0
            elif remainder >= base*2:
                res += base
            else:
                res += remainder-base+1
            # res += min(base, max(0, remainder-base+1))
            base *= 10
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 13
        expected = 6
        self.assertEqual(sol.countDigitOne(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 0
        expected = 0
        self.assertEqual(sol.countDigitOne(n), expected)
        
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
