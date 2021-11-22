import unittest
from typing import List
from pprint import pprint
import random


class Solution1:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.arr = nums[:]

    def reset(self) -> List[int]:
        self.arr = self.original[:]
        return self.arr

    def shuffle(self) -> List[int]:
        res, N = [], len(self.arr)
        while len(res) < N:
            while True:
                idx = random.randrange(0, N)
                if self.arr[idx] != None:
                    res.append(self.arr[idx])
                    self.arr[idx] = None
                    break
        self.arr = res
        return res


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.nums = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        N = len(self.nums)
        for i in range(N):
            j = random.randrange(i, N)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution([1, 2, 3, 4])
        print(sol.reset())
        print(sol.shuffle())
        print(sol.shuffle())
        print(sol.reset())
        print(sol.shuffle())
        print(sol.shuffle())
        print(sol.shuffle())
        print(sol.shuffle())
        print(sol.shuffle())
        print(sol.shuffle())
        print(sol.shuffle())
        print(sol.shuffle())

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
