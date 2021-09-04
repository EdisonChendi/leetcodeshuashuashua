import unittest
from typing import List
from pprint import pprint


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pies, nas = set(), set(), set()

        def backtrack(r, accu, res):
            if r == n:
                res.append(["."*p+"Q"+"."*(n-p-1) for p in accu])
                return res

            for c in range(n):
                if c not in cols and r+c not in pies and r-c not in nas:
                    cols.add(c)
                    pies.add(r+c)
                    nas.add(r-c)
                    accu.append(c)
                    backtrack(r+1, accu, res)
                    accu.pop()
                    cols.remove(c)
                    pies.remove(r+c)
                    nas.remove(r-c)
            return res

        return backtrack(0, [], [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 4
        expected = [[".Q..", "...Q", "Q...", "..Q."],
                    ["..Q.", "Q...", "...Q", ".Q.."]]
        self.assertCountEqual(sol.solveNQueens(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        expected = [["Q"]]
        self.assertCountEqual(sol.solveNQueens(n), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
