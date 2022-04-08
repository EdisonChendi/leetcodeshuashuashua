import collections
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        # basic approach:
        # 1. sliding window
        # 2. a balanced-BST to keep tracking of the stats of the window
        # 3. move right to expand the window
        # 4. move left to shrink the window if stats does not satisfies the requiremnts
        #    move left until right-left+1-max(bst) > k
        pass


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_f = 0
        left = 0
        counter = collections.Counter()
        for right, ch in enumerate(s):
            counter[ch] += 1
            max_f = max(max_f, counter[ch])
            if right-left+1-max_f > k:
                counter[s[left]] -= 1
                left += 1
        return right-left+1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "ABAB"
        k = 2
        expected = 4
        self.assertEqual(sol.characterReplacement(s, k), expected)

    def test_case_2(self):
        sol = Solution()
        s = "AABABBA"
        k = 1
        expected = 4
        self.assertEqual(sol.characterReplacement(s, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
