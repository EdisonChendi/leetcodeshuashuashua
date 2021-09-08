import unittest
from typing import List
from pprint import pprint
from heapq import heappush, heappop, nlargest


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))

        total_cap = w
        h, b = [], []
        for p, c in zip(profits, capital):
            heappush(h, (c, -p))

        for _ in range(k):
            while h and h[0][0] <= total_cap:
                h_top = heappop(h)
                heappush(b, (h_top[1], h_top[0]))
            if not b:
                break
            b_top = heappop(b)
            total_cap += -b_top[0]

        return total_cap


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        k = 2
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 1]
        expected = 4
        self.assertEqual(sol.findMaximizedCapital(
            k, w, profits, capital), expected)

    def test_case_2(self):
        sol = Solution()
        k = 3
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 2]
        expected = 6
        self.assertEqual(sol.findMaximizedCapital(
            k, w, profits, capital), expected)

    def test_case_3(self):
        sol = Solution()
        k = 1
        w = 2
        profits = [1, 2, 3]
        capital = [1, 1, 2]
        expected = 5
        self.assertEqual(sol.findMaximizedCapital(
            k, w, profits, capital), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
