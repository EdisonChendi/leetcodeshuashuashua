import unittest
from typing import List
from pprint import pprint


class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        i, j = 0, 0
        while i < len(s):
            idx = j % numRows if j < numRows else -2-j % numRows
            rows[idx].append(s[i])
            i += 1
            j += 1
            if j >= 2*numRows - 2:
                j = 0
        return "".join("".join(r) for r in rows)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        idx = 0
        Z = 2*numRows-2
        for i, ch in enumerate(s):
            rows[idx].append(ch)
            idx += 1 if i % Z < numRows-1 else -1
        return "".join("".join(r) for r in rows)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "PAYPALISHIRING"
        numRows = 3
        exepcted = "PAHNAPLSIIGYIR"
        self.assertEqual(sol.convert(s, numRows), exepcted)

    def test_case_2(self):
        sol = Solution()
        s = "PAYPALISHIRING"
        numRows = 4
        exepcted = "PINALSIGYAHRPI"
        self.assertEqual(sol.convert(s, numRows), exepcted)

    def test_edge_case_1(self):
        sol = Solution()
        s = "AB"
        numRows = 1
        exepcted = "AB"
        self.assertEqual(sol.convert(s, numRows), exepcted)


if __name__ == "__main__":
    unittest.main()
