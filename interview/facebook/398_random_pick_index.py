from ipaddress import collapse_addresses
import unittest
from typing import List
from pprint import pprint

import collections
import random


class Solution1:

    def __init__(self, nums: List[int]):
        self._original_nums = nums
        self.nums = collections.defaultdict(list)
        for i, n in enumerate(nums):
            self.nums[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.nums[target])


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = -1
        cnt = 0
        for i, n in enumerate(self.nums):
            if n != target:
                continue
            cnt += 1
            if random.randrange(0, cnt) == 0:
                ans = i
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
