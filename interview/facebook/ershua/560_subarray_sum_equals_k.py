import unittest
from typing import Collection, List
from pprint import pprint

import collections


class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0]
        for n in nums:
            presum.append(presum[-1]+n)
        seen = collections.Counter()
        res = 0
        for n in presum:
            res += seen[n-k]
            seen[n] += 1
        return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        res = 0
        counter = collections.Counter()
        counter[0] = 1
        for n in nums:
            comp = s+n-k
            res += counter[comp]
            s += n
            counter[s] += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
