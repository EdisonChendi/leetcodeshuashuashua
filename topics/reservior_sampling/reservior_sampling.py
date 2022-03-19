from random import random
import unittest
from typing import List
from pprint import pprint
import random


class Solution:

    def sampling(self, nums: List[int], k: int) -> List[int]:
        res = nums[:k]
        for i in range(k, len(nums)):
            n = nums[i]
            idx = random.randint(0, i)
            if idx < k:
                res[idx] = n
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        min = 0
        max = 1000
        n = 100
        nums = [random.randint(min, max) for _ in range(n)]
        print(nums)
        for _ in range(10):
            print(sorted(sol.sampling(nums, 20)))

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
