import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        count = 0
        seen = collections.defaultdict(set)

        dp = [[False, ]*N for _ in range(N)]
        for i, ch in enumerate(s):
            for j in seen[ch]:
                if i-j == 1 or dp[j+1][i-1]:
                    dp[j][i] = True
                    count += 1
            seen[ch].add(i)
            count += 1
            dp[i][i] = True

        return count


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "abc"
        expected = 3
        self.assertEqual(sol.countSubstrings(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "aaa"
        expected = 6
        self.assertEqual(sol.countSubstrings(s), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
