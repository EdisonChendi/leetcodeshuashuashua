import unittest
from typing import List
from pprint import pprint


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def palindrome(s: str) -> bool:
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j-1
            return True

        return 1 + (not palindrome(s))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "baabb"
        expected = 2
        self.assertEqual(sol.removePalindromeSub(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "ababa"
        expected = 1
        self.assertEqual(sol.removePalindromeSub(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "abb"
        expected = 2
        self.assertEqual(sol.removePalindromeSub(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
