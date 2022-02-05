import re
import unittest
from typing import List
from pprint import pprint

import heapq
import math


class Solution1:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel, ]
        stations = [[0, startFuel], ] + stations

        for i in range(1, len(stations)):
            expend = stations[i][0] - stations[i-1][0]
            refuel = stations[i][1]

            new_dp = dp[:]
            new_dp[0] = dp[0]-expend if dp[0] >= expend else -1
            new_dp.append(dp[-1]-expend+refuel if dp[-1] >= expend else -1)

            for i in range(1, len(dp)):
                new_dp[i] = max(
                    dp[i-1]-expend+refuel if dp[i-1] >= expend else -1,
                    dp[i]-expend if dp[i] >= expend else -1
                )

            dp = new_dp

        last = target-stations[-1][0]
        for i, f in enumerate(dp):
            if f >= last:
                return i
        return -1


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        tank = startFuel
        stations.append([target, -math.inf])
        refuels = []
        ans, prev = 0, 0
        for pos, ref in stations:
            tank -= pos - prev
            while refuels and tank < 0:
                tank += -heapq.heappop(refuels)
                ans += 1
            if tank < 0:
                return -1
            heapq.heappush(refuels, -ref)
            prev = pos
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        target = 100
        startFuel = 10
        stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
        expected = 2
        self.assertEqual(sol.minRefuelStops(
            target, startFuel, stations), expected)

    def test_case_2(self):
        sol = Solution()
        target = 100
        startFuel = 1
        stations = [[10, 100]]
        expected = -1
        self.assertEqual(sol.minRefuelStops(
            target, startFuel, stations), expected)

    def test_case_3(self):
        sol = Solution()
        target = 100
        startFuel = 10
        stations = [[10, 600], [20, 30], [30, 30], [60, 40]]
        expected = 1
        self.assertEqual(sol.minRefuelStops(
            target, startFuel, stations), expected)

    def test_case_4(self):
        sol = Solution()
        target = 100
        startFuel = 50
        stations = [[25, 25], [50, 50]]
        expected = 1
        self.assertEqual(sol.minRefuelStops(
            target, startFuel, stations), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
