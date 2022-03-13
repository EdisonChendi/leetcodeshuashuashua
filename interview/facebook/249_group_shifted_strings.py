import unittest
from typing import List
from pprint import pprint

import collections
# "ayz" -> "bza" -> "cab"
# "0 24 25" -> "1 25 0" -> "2 0 1"


class Solution1:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strings:
            pos = []
            move = ord(s[0])
            for ch in s:
                pos.append((ord(ch)-move) % 26)
            groups[tuple(pos)].append(s)
        return list(groups.values())


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strings:
            groups[tuple((ord(ch)-ord(s[0])) % 26 for ch in s)].append(s)
        return list(groups.values())


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
        expected = [["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]]
        self.assertCountEqual(sol.groupStrings(strings), expected)

    def test_case_2(self):
        sol = Solution()
        strings = ["a"]
        expected = [["a"]]
        self.assertCountEqual(sol.groupStrings(strings), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
