import unittest
from typing import List
from pprint import pprint
import itertools


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0, ]*n
        for f, l, s in bookings:
            res[f-1] += s
            if l < n:
                res[l] -= s
        return list(itertools.accumulate(res))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
        n = 5
        expected = [10, 55, 45, 25, 25]
        self.assertListEqual(sol.corpFlightBookings(bookings, n), expected)

    def test_case_2(self):
        sol = Solution()
        bookings = [[1, 2, 10], [2, 2, 15]]
        n = 2
        expected = [10, 25]
        self.assertListEqual(sol.corpFlightBookings(bookings, n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
