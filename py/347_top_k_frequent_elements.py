import unittest
from typing import List
from pprint import pprint
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for n, c in Counter(nums).items():
            heapq.heappush(heap, (-c, n))
        return [heapq.heappop(heap)[1] for _ in range(k)]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        self.assertListEqual(sol.topKFrequent(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1]
        k = 1
        expected = [1]
        self.assertListEqual(sol.topKFrequent(nums, k), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
