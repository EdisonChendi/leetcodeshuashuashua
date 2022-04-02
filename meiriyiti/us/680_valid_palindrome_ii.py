import unittest
from typing import List
from pprint import pprint

def palindrome(s):
    i,j = 0,len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        while i < j:
            if s[i] != s[j]:
                return palindrome(s[i+1:j+1]) or palindrome(s[i:j])
            i += 1
            j -= 1
        return True

import functools
class FollowUpSolution:

    @functools.cache
    def validPalindrome(self, s: str, n: int) -> bool:
        def palindrome(start, end, quota):
            while start < end:
                if s[start] != s[end]:
                    if quota > 0: return palindrome(start+1,end, quota-1) or palindrome(start, end-1, quota-1)
                    else: return False
                start += 1
                end -=1
            return True

        return palindrome(0, len(s)-1, n)

class TestFollowUpSolution(unittest.TestCase):
    def test_case_1(self):
        sol = FollowUpSolution()
        s = "aba"
        quota = 1
        expected = True
        self.assertEqual(sol.validPalindrome(s, quota), expected)

    def test_case_2(self):
        sol = FollowUpSolution()
        s = "aba"
        quota = 0
        expected = True
        self.assertEqual(sol.validPalindrome(s, quota), expected)

    def test_case_3(self):
        sol = FollowUpSolution()
        s = "abaaa"
        quota = 0
        expected = False
        self.assertEqual(sol.validPalindrome(s, quota), expected)

    def test_case_3(self):
        sol = FollowUpSolution()
        s = "abcad"
        quota = 1
        expected = False
        self.assertEqual(sol.validPalindrome(s, quota), expected)

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "aba"
        expected = True
        self.assertEqual(sol.validPalindrome(s), expected)
        
    def test_case_2(self):
        sol = Solution()
        s = "abca"
        expected = True
        self.assertEqual(sol.validPalindrome(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "abc"
        expected = False
        self.assertEqual(sol.validPalindrome(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
