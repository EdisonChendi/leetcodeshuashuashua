import unittest
from typing import List
from pprint import pprint
import bisect
import collections


class Solution2:
    def shortestWay(self, source: str, target: str) -> int:
        # by greedy
        if set(target) - set(source):
            return -1
        test = source
        i, j = 0, 0
        res = 1
        while j < len(target):
            if i == len(test):
                test += source
                res += 1
            if test[i] == target[j]:
                j += 1
            i += 1
        return res


class Solution:
    def shortestWay(self, source, target):
        char_indices = collections.defaultdict(list)
        for i, c in enumerate(source):
            char_indices[c].append(i)

        result = 0
        i = 0  # next index of source to check

        for c in target:
            if c not in char_indices:  # cannot make target if char not in source
                return -1

            # index in char_indices[c] that is >= i
            j = bisect.bisect_left(char_indices[c], i)
            # wrap around to beginning of source
            if j == len(char_indices[c]):
                result += 1
                j = 0
            i = char_indices[c][j] + 1  # next index in source

        return result if i == 0 else result + 1  # add 1 for partial source


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        source = "abc"
        target = "abcbc"
        expected = 2
        self.assertEqual(sol.shortestWay(source, target), expected)

    def test_case_2(self):
        sol = Solution()
        source = "abc"
        target = "acdbc"
        expected = -1
        self.assertEqual(sol.shortestWay(source, target), expected)

    def test_case_3(self):
        sol = Solution()
        source = "xyz"
        target = "xzyxz"
        expected = 3
        self.assertEqual(sol.shortestWay(source, target), expected)

    def test_case_4(self):
        sol = Solution()
        source = "adbsc"
        target = "addddddddddddsbc"
        expected = 13
        self.assertEqual(sol.shortestWay(source, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
