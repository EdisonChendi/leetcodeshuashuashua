import unittest
from typing import List
from pprint import pprint

from sortedcontainers import SortedList

import heapq


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = SortedList(range(k))
        busy = []
        stats = [0]*k
        max_cnt = 0
        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                free.add(busy[0][1])
                heapq.heappop(busy)

            if not free:
                continue

            idx = free.bisect_left(i % k) % len(free)
            chosen = free[idx]
            free.remove(chosen)
            heapq.heappush(busy, (a+l, chosen))

            stats[chosen] += 1
            max_cnt = max(max_cnt, stats[chosen])

        return [i for i in range(k) if stats[i] == max_cnt]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        k = 3
        arrival = [1, 2, 3, 4, 5]
        load = [5, 2, 3, 3, 3]
        expected = [1]
        self.assertCountEqual(sol.busiestServers(k, arrival, load), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
