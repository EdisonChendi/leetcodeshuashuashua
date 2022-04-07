from itertools import count
import unittest
from typing import List
from pprint import pprint

import collections


class Solution1:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        counter = collections.Counter()
        res = 0
        for right, ch in enumerate(s):
            counter[ch] += 1
            while len(counter) > k:
                ch_left = s[left]
                counter[ch_left] -= 1
                if counter[ch_left] == 0:
                    counter.pop(ch_left)
                left += 1
            res = max(res, right-left+1)
        return res


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = {}
        res = 0
        left = 0
        for right, ch in enumerate(s):
            d[ch] = right
            if len(d) > k:
                left = min(d.values())
                del d[s[left]]
                left += 1
            res = max(res, right-left+1)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "eceba"
        k = 2
        expected = 3
        self.assertEqual(sol.lengthOfLongestSubstringKDistinct(s, k), expected)

    def test_case_2(self):
        sol = Solution()
        s = "aa"
        k = 1
        expected = 2
        self.assertEqual(sol.lengthOfLongestSubstringKDistinct(s, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
