import unittest
from typing import List
from pprint import pprint
import collections


class Solution1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ns = sorted(collections.Counter(nums).items())
        y, n = ns[0][0]*ns[0][1], 0
        for i in range(1, len(ns)):
            cur, last = ns[i], ns[i-1]
            if last[0] == cur[0]-1:
                y, n = n+cur[0]*cur[1], max(y, n)
            else:
                y, n = max(y, n)+cur[0]*cur[1], max(y, n)
        return max(y, n)


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def rob(nums: List[int]) -> int:
            y, n = 0, 0
            for m in nums:
                y, n = n+m, max(y, n)
            return max(y, n)

        max_val = max(nums)
        vals = [0]*(max_val+1)
        for n in nums:
            vals[n] += n

        return rob(vals)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3, 4, 2]
        expected = 6
        self.assertEqual(sol.deleteAndEarn(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [2, 2, 3, 3, 3, 4]
        expected = 9
        self.assertEqual(sol.deleteAndEarn(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
