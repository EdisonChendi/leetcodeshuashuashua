import unittest
from typing import List
from pprint import pprint


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "A man, a plan, a canal: Panama"
        expected = True
        self.assertEqual(sol.isPalindrome(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "race a car"
        expected = False
        self.assertEqual(sol.isPalindrome(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
