import random
from ast import operator
import unittest
from typing import List
from pprint import pprint

import collections
import heapq


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # naive heap
        counter = [(-cnt, n) for n, cnt in collections.Counter(nums).items()]
        heapq.heapify(counter)  # O(N)
        return [heapq.heappop(counter)[1] for _ in range(k)]  # (klogN)


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap of size k - O(Nlgk)
        counter = collections.Counter(nums)
        h = []
        for n, cnt in counter.items():
            if len(h) < k:
                heapq.heappush(h, (cnt, n))
            else:
                if cnt > h[0][0]:
                    heapq.heappushpop(h, (cnt, n))
        return [n for _, n in h]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # quick select
        # O(N)
        counter = [(cnt, n) for n, cnt in collections.Counter(nums).items()]
        N = len(counter)
        self.quickselect(counter, 0, N-1, N-k)
        return [counter[i][1] for i in range(N-k, N)]

    def quickselect(self, nums, left, right, k):
        idx = self.partition(nums, left, right, k)
        if idx == k:
            return

        if idx > k:
            self.quickselect(nums, left, idx-1, k)
        else:
            self.quickselect(nums, idx+1, right, k)

    def partition(self, nums, left, right, k):
        rand_idx = random.randint(left, right)
        chosen = nums[rand_idx]
        nums[rand_idx], nums[right] = nums[right], nums[rand_idx]
        i = 0
        for j in range(right):
            if nums[j][0] < chosen[0]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[right], nums[i] = nums[i], nums[right]
        return i


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        self.assertCountEqual(sol.topKFrequent(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1]
        k = 1
        expected = [1]
        self.assertCountEqual(sol.topKFrequent(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
