import unittest
from typing import List
from pprint import pprint

import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)

        def t(s):
            return tuple((ord(s[i+1])-ord(s[i])) % 26 for i in range(len(s)-1))

        for s in strings:
            d[t(s)].append(s)

        return list(d.values())


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
