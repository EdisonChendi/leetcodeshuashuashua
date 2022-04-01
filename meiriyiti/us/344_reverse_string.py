import unittest
from typing import List
from pprint import pprint

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i,j = 0,len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = ["h","e","l","l","o"]
        expected = ["o","l","l","e","h"]
        sol.reverseString(s)
        self.assertListEqual(s, expected)

    def test_case_2(self):
        sol = Solution()
        s = ["H","a","n","n","a","h"]
        expected = ["h","a","n","n","a","H"]
        sol.reverseString(s)
        self.assertListEqual(s, expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
