import unittest
from typing import List
from pprint import pprint


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        N = len(s)
        i, j = N-1, N-1
        while i >= 0 and s[i] == " ":
            i, j = i-1, j-1
        while i >= 0 and s[i] != " ":
            i -= 1
        return j - i

    def lengthOfLastWord1(self, s: str) -> int:
        l = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and l > 0:
                return l
            if s[i] != " ":
                l += 1
        return l


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "   fly me   to   the moon  "
        expected = 4
        self.assertEqual(sol.lengthOfLastWord(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "luffy is still joyboy"
        expected = 6
        self.assertEqual(sol.lengthOfLastWord(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
