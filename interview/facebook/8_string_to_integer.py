import unittest
from typing import List
from pprint import pprint


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        i = 0
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = 1 if s[i] == '+' else -1
            i += 1
        n = 0
        while i < len(s) and s[i].isdigit():
            if sign == 1 and (2**31-1-int(s[i]))/10 <= n:
                return 2**31-1
            if sign == -1 and (2**31-int(s[i]))/10 <= n:
                return -2**31
            n = n*10+int(s[i])
            i += 1
        return sign * n


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "42"
        expected = 42
        self.assertEqual(sol.myAtoi(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "  -42"
        expected = -42
        self.assertEqual(sol.myAtoi(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "4193 with words"
        expected = 4193
        self.assertEqual(sol.myAtoi(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
