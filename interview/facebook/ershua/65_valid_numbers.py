import re
from code import interact
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def isNumber1(self, s: str) -> bool:
        digit = exponent = dot = False
        for i, ch in enumerate(s):
            if ch.isdigit():
                digit = True
            elif ch in 'eE':
                if exponent or not digit:
                    return False
                exponent = True
                digit = False
            elif ch in "+-":
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif ch == '.':
                if exponent or dot:
                    return False
                dot = True
            else:
                return False
        return digit


class Solution2:
    def isNumber(self, s: str) -> bool:
        def decimal(s):
            return bool(re.match("^[+-]?(\d+\.|\d+\.\d+|\.\d+)$", s))

        def integer(s):
            return bool(re.match("^[+-]?\d+$", s))

        arr = s.lower().split('e')
        if len(arr) > 2:
            return False

        elif len(arr) == 1:
            return decimal(s) or integer(s)

        elif len(arr) == 2:
            a, b = arr
            return (decimal(a) or integer(a)) and integer(b)


class Solution:
    def isNumber(self, s: str) -> bool:
        dfs = [
            {"sign": 1, "digit": 2, "dot": 3},
            {"dot": 3, "digit": 2},
            {"digit": 2, "dot": 4, "expo": 5},
            {"digit": 4},
            {"digit": 4, "expo": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7}
        ]

        state = 0
        for ch in s:
            action = ""
            if ch in "+-":
                action = "sign"
            elif ch.isdigit():
                action = "digit"
            elif ch == ".":
                action = "dot"
            elif ch in "eE":
                action = "expo"

            if action not in dfs[state]:
                return False

            state = dfs[state][action]

        return state in {2, 4, 7}


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
