from nis import match
import unittest
from typing import List
from pprint import pprint

import collections


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all_players = set()
        lose_counter = collections.Counter()
        for w, l in matches:
            all_players.add(w)
            all_players.add(l)
            lose_counter[l] += 1

        ans0 = list(all_players - set(lose_counter.keys()))
        ans1 = [p for p, cnt in lose_counter.items() if cnt == 1]
        return [sorted(ans0), sorted(ans1)]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
                   [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
        expected = [[1, 2, 10], [4, 5, 7, 8]]
        self.assertCountEqual(sol.findWinners(matches), expected)

    def test_case_2(self):
        sol = Solution()
        matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
        expected = [[1, 2, 5, 6], []]
        self.assertCountEqual(sol.findWinners(matches), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
