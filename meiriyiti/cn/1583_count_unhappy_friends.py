import unittest
from typing import List
from pprint import pprint
from collections import defaultdict


def cal_scores(preferences, n):
    scores = defaultdict(defaultdict)
    for i, pref in enumerate(preferences):
        for j, p in enumerate(pref):
            scores[i][p] = n-1-j
    return scores


def gen_pairs_mapping(pairs):
    m = {}
    for i, j in pairs:
        m[i] = j
        m[j] = i
    return m


def is_unhappy(preferences, scores, pairs, i):
    pairing = pairs[i]
    for friend in preferences[i]:
        if friend == pairing:
            return False
        friend_pair = pairs[friend]
        friend_scores = scores[friend]
        if friend_scores[i] > friend_scores[friend_pair]:
            return True


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        scores = cal_scores(preferences, n)
        pairs = gen_pairs_mapping(pairs)
        # unhappy_count = 0
        # for i in range(n):
        #     if is_unhappy(preferences, scores, pairs, i):
        #         unhappy_count += 1
        # return unhappy_count
        return sum(is_unhappy(preferences, scores, pairs, i) for i in range(n))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 4
        preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
        pairs = [[0, 1], [2, 3]]
        expected = 2
        self.assertEqual(sol.unhappyFriends(n, preferences, pairs), expected)

    def test_case_2(self):
        sol = Solution()
        n = 2
        preferences = [[1], [0]]
        pairs = [[1, 0]]
        expected = 0
        self.assertEqual(sol.unhappyFriends(n, preferences, pairs), expected)

    def test_case_3(self):
        sol = Solution()
        n = 4
        preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
        pairs = [[1, 3], [0, 2]]
        expected = 4
        self.assertEqual(sol.unhappyFriends(n, preferences, pairs), expected)
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
