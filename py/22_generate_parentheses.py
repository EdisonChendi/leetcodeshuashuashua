import unittest
from typing import List
from pprint import pprint


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def sub(l, r, n, cur, res):
            # if r == n:  # enough
            if l == n and r == n:
                res.append(cur)
                return res

            if l < n:
                sub(l+1, r, n, cur+"(", res)
            if r < l:
                sub(l, r+1, n, cur+")", res)

            return res

        return sub(0, 0, n, "", [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        res = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertCountEqual(sol.generateParenthesis(n), res)

    def test_case_2(self):
        sol = Solution()
        n = 1
        res = ["()"]
        self.assertCountEqual(sol.generateParenthesis(n), res)

    def test_case_3(self):
        sol = Solution()
        n = 2
        res = ["()()", "(())"]
        self.assertCountEqual(sol.generateParenthesis(n), res)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
