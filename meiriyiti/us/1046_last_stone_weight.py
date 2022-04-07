import unittest
from typing import List
from pprint import pprint

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = []
        for s in stones:
            heapq.heappush(l, -s)

        while len(l) > 1:
            s1 = -heapq.heappop(l)
            s2 = -heapq.heappop(l)
            if s1 != s2:
                heapq.heappush(l, s2-s1)

        return -l[0] if l else 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        stones = [2, 7, 4, 1, 8, 1]
        expected = 1
        self.assertEqual(sol.lastStoneWeight(stones), expected)

    def test_case_2(self):
        sol = Solution()
        stones = [1]
        expected = 1
        self.assertEqual(sol.lastStoneWeight(stones), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
