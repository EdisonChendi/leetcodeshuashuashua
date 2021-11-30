import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp = len(s), len(p)
        if ls < lp:
            return []

        counter = collections.Counter(p)
        for i in range(lp):
            ch = s[i]
            counter[ch] -= 1
            if counter[ch] == 0:
                counter.pop(ch)

        res = []
        if not counter:
            res.append(0)

        for i in range(ls-lp):
            l = s[i]
            counter[l] += 1
            if counter[l] == 0:
                counter.pop(l)

            r = s[i+lp]
            counter[r] -= 1
            if counter[r] == 0:
                counter.pop(r)

            if not counter:
                res.append(i+1)

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "cbaebabacd"
        p = "abc"
        expected = [0, 6]
        self.assertListEqual(sol.findAnagrams(s, p), expected)

    def test_case_2(self):
        sol = Solution()
        s = "abab"
        p = "ab"
        expected = [0, 1, 2]
        self.assertListEqual(sol.findAnagrams(s, p), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
