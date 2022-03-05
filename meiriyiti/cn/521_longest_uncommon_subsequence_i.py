import unittest
from typing import List
from pprint import pprint


class Solution1:
    def findLUSlength(self, a: str, b: str) -> int:
        la = len(a)
        lb = len(b)
        if la != lb:
            return max(la, lb)
        else:
            return la if a != b else -1


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        a = "aba"
        b = "cdc"
        expected = 3
        self.assertEqual(sol.findLUSlength(a, b), expected)

    def test_case_2(self):
        sol = Solution()
        a = "aaa"
        b = "bbb"
        expected = 3
        self.assertEqual(sol.findLUSlength(a, b), expected)

    def test_case_3(self):
        sol = Solution()
        a = "aaa"
        b = "aaa"
        expected = -1
        self.assertEqual(sol.findLUSlength(a, b), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
