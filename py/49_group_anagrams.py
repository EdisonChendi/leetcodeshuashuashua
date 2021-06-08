from collections import defaultdict
import unittest
from typing import List
from pprint import pprint

from collections import defaultdict


class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[str(sorted(s))].append(s)
        return list(res.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            table = [0, ]*26
            for ch in s:
                table[ord(ch)-ord("a")] += 1
            res[tuple(table)].append(s)
        return list(res.values())


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        print(sol.groupAnagrams(strs))
        # self.assertListEqual(sol.groupAnagrams(strs), expected)

    def test_case_2(self):
        sol = Solution()
        strs = [""]
        expected = [[""]]
        print(sol.groupAnagrams(strs))
        # self.assertCountEqual(sol.groupAnagrams(strs), expected)

    def test_case_3(self):
        sol = Solution()
        strs = ["a"]
        expected = [["a"]]
        print(sol.groupAnagrams(strs))
        # self.assertCountEqual(sol.groupAnagrams(strs), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
