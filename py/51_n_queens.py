import unittest
from typing import List
from pprint import pprint


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pies, nas, cols = set(), set(), set()

        def backtrack(level, cur, accu):
            if level == n:
                accu.append(["."*i + "Q"+"."*(n-i-1) for i in cur])
                return accu

            for c in range(n):
                pie = c + level
                na = c - level

                if pie in pies or na in nas or c in cols:
                    continue

                cur.append(c)
                pies.add(pie)
                nas.add(na)
                cols.add(c)

                backtrack(level+1, cur, accu)

                cur.pop()
                pies.remove(pie)
                nas.remove(na)
                cols.remove(c)

            return accu

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
