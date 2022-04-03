import unittest
from typing import List
from pprint import pprint

import bisect


class Solution1:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect.bisect_right(letters, target) % len(letters)]


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)
        l = 0
        r = len(letters)-1
        while l <= r:
            m = (l+r) >> 1
            mid = letters[m]
            if mid <= target:
                l = m + 1
            else:
                r = m - 1
        return letters[l % N]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        letters = ["c", "f", "j"]
        target = "a"
        expected = "c"
        self.assertEqual(sol.nextGreatestLetter(letters, target), expected)

    def test_case_2(self):
        sol = Solution()
        letters = ["c", "f", "j"]
        target = "c"
        expected = "f"
        self.assertEqual(sol.nextGreatestLetter(letters, target), expected)

    def test_case_3(self):
        sol = Solution()
        letters = ["c", "f", "j"]
        target = "d"
        expected = "f"
        self.assertEqual(sol.nextGreatestLetter(letters, target), expected)

    def test_case_4(self):
        sol = Solution()
        letters = ["c", "f", "j"]
        target = "k"
        expected = "c"
        self.assertEqual(sol.nextGreatestLetter(letters, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
