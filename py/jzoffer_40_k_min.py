import unittest
from typing import List
from pprint import pprint
import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        heapq.heapify(arr)
        return [heapq.heappop(arr) for _ in range(k)]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [3, 2, 1]
        k = 2
        expected = [1, 2]
        self.assertListEqual(sol.getLeastNumbers(arr, k), expected)

    def test_case_2(self):
        sol = Solution()
        arr = [0, 1, 2, 1]
        k = 1
        expected = [0]
        self.assertListEqual(sol.getLeastNumbers(arr, k), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
