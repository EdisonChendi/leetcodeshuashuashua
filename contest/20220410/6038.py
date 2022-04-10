import unittest
from typing import List
from pprint import pprint

import math

import functools


class Solution1:
    def minimizeResult(self, expression: str) -> str:
        # res = math.inf

        @functools.cache
        def dfs(i, j):
            # nonlocal res

            if i < 0 or j > L2:
                return math.inf

            # left part
            l1 = 1 if i == 0 else int(l[:i])
            l2 = int(l[i:])

            # right part
            r1 = int(r[:j])
            r2 = 1 if j == L2 else int(r[j:])

            exp_res = l1*(l2+r1)*r2
            # res = min(exp_res, res)

            r1 = dfs(i-1, j)
            r2 = dfs(i, j+1)

            return min(exp_res, r1, r2)

        l, r = expression.split("+")
        L1 = len(l)
        L2 = len(r)
        return dfs(L1-1, 1)

        # return res


class Solution:
    def minimizeResult(self, expression: str) -> str:
        # res = math.inf
        res_i, res_j = 0, 0
        min_ = math.inf

        @functools.cache
        def dfs(i, j):
            nonlocal min_, res_i, res_j

            if i < 0 or j > L2:
                return math.inf

            # left part
            l1 = 1 if i == 0 else int(l[:i])
            l2 = int(l[i:])

            # right part
            r1 = int(r[:j])
            r2 = 1 if j == L2 else int(r[j:])

            exp_res = l1*(l2+r1)*r2
            if exp_res < min_:
                min_ = exp_res
                res_i, res_j = i, j

            r1 = dfs(i-1, j)
            r2 = dfs(i, j+1)

            return min(exp_res, r1, r2)

        l, r = expression.split("+")
        L1 = len(l)
        L2 = len(r)
        dfs(L1-1, 1)
        l_res = "(".join((l[:res_i], l[res_i:]))
        r_res = ")".join((r[:res_j], r[res_j:]))
        return "+".join((l_res, r_res))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        expression = "247+38"
        expected = "2(47+38)"
        self.assertEqual(sol.minimizeResult(expression), expected)

    def test_case_2(self):
        sol = Solution()
        expression = "12+34"
        expected = "1(2+3)4"
        self.assertEqual(sol.minimizeResult(expression), expected)

    def test_case_3(self):
        sol = Solution()
        expression = "999+999"
        expected = "(999+999)"
        self.assertEqual(sol.minimizeResult(expression), expected)
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
