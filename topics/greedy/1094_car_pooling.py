import unittest
from typing import List
from pprint import pprint


class Solution1:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0]*1001
        for n, f, t in trips:
            arr[f] += n
            arr[t] -= n

        cur = 0
        for n in arr:
            cur += n
            if cur > capacity:
                return False
        return True


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        N = len(trips)
        stops = []
        for n, f, t in trips:
            stops.append((f, n))
            stops.append((t, -n))

        stops.sort()
        accu = 0
        for _, n in stops:
            accu += n
            if accu > capacity:
                return False
        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 4
        expected = False
        self.assertEqual(sol.carPooling(trips, capacity), expected)

    def test_case_2(self):
        sol = Solution()
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 5
        expected = True
        self.assertEqual(sol.carPooling(trips, capacity), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
