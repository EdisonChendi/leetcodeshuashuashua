import unittest
from typing import List
from pprint import pprint

import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:
            heapq.heappush(self.arr, val)
        else:
            if val > self.arr[0]:
                heapq.heappushpop(self.arr, val)
        return self.arr[0]

    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
