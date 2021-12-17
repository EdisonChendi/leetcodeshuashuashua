import unittest
from typing import List
from pprint import pprint


class Solution1:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res, full, empty = 0, numBottles, 0
        while full > 0:
            res += full
            empty += full
            full, empty = divmod(empty, numExchange)
        return res


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        numBottles = 9
        numExchange = 3
        expected = 13
        self.assertEqual(sol.numWaterBottles(
            numBottles, numExchange), expected)

    def test_case_2(self):
        sol = Solution()
        numBottles = 15
        numExchange = 4
        expected = 19
        self.assertEqual(sol.numWaterBottles(
            numBottles, numExchange), expected)

    def test_case_3(self):
        sol = Solution()
        numBottles = 5
        numExchange = 5
        expected = 6
        self.assertEqual(sol.numWaterBottles(
            numBottles, numExchange), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
