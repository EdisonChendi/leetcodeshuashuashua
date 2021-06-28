import unittest
from typing import List
from pprint import pprint


mapping = {
    "2": list("abc"),
    "3": list("def"),
    "4": list("ghi"),
    "5": list("jkl"),
    "6": list("mno"),
    "7": list("pqrs"),
    "8": list("tuv"),
    "9": list("wxyz")
}


class Solution:
    def letterCombinations1(self, digits: str) -> List[str]:
        def sub(digits):
            if not digits:
                return ["", ]
            return [ch + comb for ch in mapping[digits[0]] for comb in sub(digits[1:])]

        if not digits:
            return []
        return sub(digits)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        h, t = digits[0], digits[1:]
        if not t:
            return mapping[h]
        else:
            return [ch+comb for ch in mapping[h] for comb in self.letterCombinations(t)]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertCountEqual(sol.letterCombinations(digits), expected)

    def test_case_2(self):
        sol = Solution()
        digits = "2"
        expected = ["a", "b", "c"]
        self.assertCountEqual(sol.letterCombinations(digits), expected)

    def test_edge_case_1(self):
        sol = Solution()
        digits = ""
        expected = []
        self.assertCountEqual(sol.letterCombinations(digits), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
