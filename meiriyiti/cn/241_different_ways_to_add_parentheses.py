from cmath import exp
import unittest
from typing import List
from pprint import pprint
import functools

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        ops = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b
        }

        @functools.cache
        def helper(l, r):
            res = []
            for i in range(l+1, r):
                op = expression[i]
                if op in ops.keys():
                    f = ops[op]
                    for lv in helper(l, i-1):
                        for rv in helper(i+1, r):
                            res.append(f(lv, rv))
            if not res:
                res.append(int(expression[l:r+1]))
            return res
        
        return helper(0, len(expression)-1)

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        expression = "2-1-1"
        expected = [0,2]
        self.assertCountEqual(sol.diffWaysToCompute(expression), expected)

    def test_case_2(self):
        sol = Solution()
        expression = "2*3-4*5"
        expected = [-34,-14,-10,-10,10]
        self.assertCountEqual(sol.diffWaysToCompute(expression), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
