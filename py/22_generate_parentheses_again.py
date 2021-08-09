import unittest
from typing import List
from pprint import pprint


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def sub(l, r, accu, res):
            if l == 0 and r == 0:
                res.append(accu)
                return res

            if l > 0:
                sub(l-1, r, accu+"(", res)
            if l < r:
                sub(l, r-1, accu+")", res)
            return res

        return sub(n, n, "", [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertCountEqual(sol.generateParenthesis(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        expected = ["()"]
        self.assertCountEqual(sol.generateParenthesis(n), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
