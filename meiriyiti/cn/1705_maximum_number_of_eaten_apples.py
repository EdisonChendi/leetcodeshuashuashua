import unittest
from typing import List
from pprint import pprint
import heapq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        h = []
        res = 0
        day = 0
        for a, d in zip(apples, days):
            # get rid of rotten apples
            while h and h[0][0] <= day:
                heapq.heappop(h)

            # pick up today's apples
            if a > 0 and d > 0:
                heapq.heappush(h, (d+day, a))

            # choose the one that closest to rot
            if h and h[0][0] > day:
                eat = heapq.heappop(h)
                res += 1
                if eat[1]-1 > 0:
                    heapq.heappush(h, (eat[0], eat[1]-1))

            day += 1

        # left apples
        while h:
            exp, cnt = heapq.heappop(h)
            can_eat = min(cnt, exp-day)
            res += can_eat
            day += can_eat

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        apples = [1, 2, 3, 5, 2]
        days = [3, 2, 1, 4, 2]
        expected = 7
        self.assertEqual(sol.eatenApples(apples, days), expected)

    def test_case_2(self):
        sol = Solution()
        apples = [3, 0, 0, 0, 0, 2]
        days = [3, 0, 0, 0, 0, 2]
        expected = 5
        self.assertEqual(sol.eatenApples(apples, days), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
