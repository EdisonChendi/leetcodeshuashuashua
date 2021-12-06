import unittest
from typing import List
from pprint import pprint

class Solution1:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        i,N = 0,len(s)
        while k > 0 and i < N:
            k -= s[i] == " "
            i += 1
        return s[:i-1] if k == 0 else s


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "Hello how are you Contestant"; k = 4
        expected = "Hello how are you"
        self.assertEqual(sol.truncateSentence(s, k), expected)

    def test_case_2(self):
        sol = Solution()
        s = "What is the solution to this problem"; k = 4
        expected = "What is the solution"
        self.assertEqual(sol.truncateSentence(s, k), expected)

    def test_case_3(self):
        sol = Solution()
        s = "chopper is not a tanuki"; k = 5
        expected = "chopper is not a tanuki"
        self.assertEqual(sol.truncateSentence(s, k), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
