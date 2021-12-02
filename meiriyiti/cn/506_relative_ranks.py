import unittest
from typing import List
from pprint import pprint


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sorted = {s: i+1 for i,
                        s in enumerate(sorted(score, reverse=True))}
        mapping = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}

        def rank_mapper(s):
            pos = score_sorted[s]
            return mapping.get(pos, str(pos))

        return [rank_mapper(s) for s in score]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        score = [5, 4, 3, 2, 1]
        expected = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
        self.assertListEqual(sol.findRelativeRanks(score), expected)

    def test_case_2(self):
        sol = Solution()
        score = [10, 3, 8, 9, 4]
        expected = ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
        self.assertListEqual(sol.findRelativeRanks(score), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
