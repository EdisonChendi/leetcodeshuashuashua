import enum
import unittest
from typing import List
from pprint import pprint

import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        o = {ch: i for i, ch in enumerate(order)}
        counter = collections.Counter()
        others = []
        for ch in s:
            if ch in o:
                counter[o[ch]] += 1
            else:
                others.append(ch)
        return "".join(("".join(order[i]*counter[i] for i in range(len(order))), "".join(others)))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        order = "cba"
        s = "abcd"
        expected = "cbad"
        self.assertEqual(sol.customSortString(order, s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
