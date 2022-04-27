import random
from curses import pair_content
import unittest
from typing import List
from pprint import pprint

import collections
import heapq


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap
        # Time: O(Nlgk)
        # Space: O(N)
        counter = [(cnt, n) for n, cnt in collections.Counter(nums).items()]
        h = []
        for ele in counter:
            if len(h) < k:
                heapq.heappush(h, ele)
                continue
            if ele[0] > h[0][0]:
                heapq.heappushpop(h, ele)
        return [n for _, n in h]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Quick Select

        def partition(counter, l, r):
            idx = random.randint(l, r)
            counter[r], counter[idx] = counter[idx], counter[r]
            j = l
            for i in range(l, r):
                if counter[i][0] < counter[r][0]:
                    counter[i], counter[j] = counter[j], counter[i]
                    j += 1
            counter[r], counter[j] = counter[j], counter[r]
            return j

        def quick_select(counter, k):

            l, r = 0, len(counter)-1
            idx = partition(counter, l, r)

            while idx != k:
                if idx > k:
                    r = idx-1
                else:
                    l = idx+1
                idx = partition(counter, l, r)

        counter = [(cnt, n)
                   for n, cnt in collections.Counter(nums).items()]

        quick_select(counter, len(counter)-k)
        return [n for _, n in counter[len(counter)-k:]]


class TestSolution(unittest.TestCase):

    # def test_case_1(self):
    #     sol = Solution()
    #     nums = [1, 1, 1, 2, 2, 3]
    #     k = 2
    #     print(sol.topKFrequent(nums, k))

    def test_case_2(self):
        sol = Solution()
        nums = [1]
        k = 1
        print(sol.topKFrequent(nums, k))

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
