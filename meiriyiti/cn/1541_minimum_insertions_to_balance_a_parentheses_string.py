import unittest
from typing import List
from pprint import pprint


class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        open = 0
        N = len(s)
        i = 0
        while i < N:
            ch = s[i]
            if ch == '(':
                open += 1
                i += 1
            else:
                if i < N-1:
                    nxt_ch = s[i+1]
                    if nxt_ch == ')':
                        if open > 0:
                            open -= 1
                        else:
                            ans += 1
                        i += 2
                    else:
                        if open > 0:
                            ans += 1
                            open -= 1
                        else:
                            ans += 2
                        i += 1
                else:
                    if open > 0:
                        ans += 1
                        open -= 1
                    else:
                        ans += 2
                    i += 1
        return ans + open * 2


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "(()))"
        expected = 1
        self.assertEqual(sol.minInsertions(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "())"
        expected = 0
        self.assertEqual(sol.minInsertions(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "))())("
        expected = 3
        self.assertEqual(sol.minInsertions(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
