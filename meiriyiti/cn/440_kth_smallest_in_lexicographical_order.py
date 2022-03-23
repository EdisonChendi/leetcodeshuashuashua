import unittest
from typing import List
from pprint import pprint

import heapq

class Solution1:
    # LTE
    def findKthNumber(self, n: int, k: int) -> int:
        h = list(map(str,range(1,n+1)))
        heapq.heapify(h)
        for _ in range(k-1):
            heapq.heappop(h)
        return int(heapq.heappop(h))


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def steps(cur, n):
            res = 0
            first = last = cur
            while first <= n:
                res += min(n,last)-first+1
                first = 10*first
                last = 10*last+9
            return res

        cur = 1
        i = 1
        while i < k:
            cnt = steps(cur, n)
            if i + cnt <= k:
                i += cnt
                cur += 1
            else:
                i += 1
                cur *= 10
        return cur


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 13
        k = 2
        expected = 10
        self.assertEqual(sol.findKthNumber(n,k), expected)
        
    def test_case_2(self):
        sol = Solution()
        n = 1
        k = 1
        expected = 1
        self.assertEqual(sol.findKthNumber(n,k), expected)
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
