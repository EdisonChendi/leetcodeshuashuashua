import unittest
from typing import List
from pprint import pprint
from bisect import bisect_right


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes = [0]*len(persons)
        self.times = times
        self.tops = []
        top = 0
        for p in persons:
            self.votes[p] += 1
            if self.votes[p] >= self.votes[top]:
                top = p
            self.tops.append(top)

    def q(self, t: int) -> int:
        return self.tops[bisect_right(self.times, t)-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        tvc = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [
                                0, 5, 10, 15, 20, 25, 30])
        self.assertEqual(tvc.q(3), 0)
        self.assertEqual(tvc.q(12), 1)
        self.assertEqual(tvc.q(25), 1)
        self.assertEqual(tvc.q(15), 0)
        self.assertEqual(tvc.q(24), 0)
        self.assertEqual(tvc.q(8), 1)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
