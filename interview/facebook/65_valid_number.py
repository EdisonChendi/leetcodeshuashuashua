import unittest
from typing import List
from pprint import pprint


def valid_int(num, allow_empty=False):
    if not allow_empty and not num:
        return False
    j = 0
    while j < len(num):
        if not num[j].isdigit():
            return False
        j += 1
    return True


class Solution:
    def isNumber(self, s: str) -> bool:
        OP = {'+', '-'}
        N = len(s)
        # read to e
        # should be a valid decimal
        i = 0
        if s[i] in OP:
            i += 1
            if i == N:
                return False

        decimal = []
        while i < N and s[i].lower() != 'e':
            decimal.append(s[i])
            i += 1

        parts = "".join(decimal).split(".")
        if len(parts) == 1:
            if not valid_int(parts[0]):
                return False
        elif len(parts) == 2:
            if not parts[0] and not parts[1]:
                return False
            if not valid_int(parts[0], allow_empty=True) or not valid_int(parts[1], allow_empty=True):
                return False
        else:
            return False

        if i == N:
            return True

        # read to end
        # should be a valid integer
        i += 1
        if i == N:
            return False

        if s[i] in OP:
            i += 1
            if i == N:
                return False

        if not valid_int(s[i:]):
            return False

        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "0"
        expected = True
        self.assertEqual(sol.isNumber(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "e"
        expected = False
        self.assertEqual(sol.isNumber(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "."
        expected = False
        self.assertEqual(sol.isNumber(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "-0.1"
        expected = True
        self.assertEqual(sol.isNumber(s), expected)

    def test_case_5(self):
        sol = Solution()
        s = "+3.11e-7"
        expected = True
        self.assertEqual(sol.isNumber(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
