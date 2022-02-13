import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(ch for ch in text if ch in "balloon")
        return min(cnt['b'], cnt['a'], cnt['l']//2, cnt['o']//2, cnt['n'])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        text = "nlaebolko"
        expected = 1
        self.assertEqual(sol.maxNumberOfBalloons(text), expected)

    def test_case_2(self):
        sol = Solution()
        text = "loonbalxballpoon"
        expected = 2
        self.assertEqual(sol.maxNumberOfBalloons(text), expected)

    def test_case_3(self):
        sol = Solution()
        text = "leetcode"
        expected = 0
        self.assertEqual(sol.maxNumberOfBalloons(text), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
