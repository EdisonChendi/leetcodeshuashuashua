import unittest
from typing import List
from pprint import pprint


class Solution1:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        a, A, Z = ord('a'), ord('A'), ord('Z')
        for ch in s:
            c = ord(ch)
            if A <= c <= Z:
                res.append(chr(c-A+a))
            else:
                res.append(ch)
        return "".join(res)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "Hello"
        expected = "hello"
        self.assertEqual(sol.toLowerCase(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "here"
        expected = "here"
        self.assertEqual(sol.toLowerCase(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "LOVELY"
        expected = "lovely"
        self.assertEqual(sol.toLowerCase(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "LOV1ELY"
        expected = "lov1ely"
        self.assertEqual(sol.toLowerCase(s), expected)
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
