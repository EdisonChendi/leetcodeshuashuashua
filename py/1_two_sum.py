import unittest
from typing import List
from pprint import pprint


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        for i, n in enumerate(nums):
            v = target - n
            if v in rem:
                return [rem[v], i]
            rem[n] = i
        return []


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertListEqual(sol.twoSum(nums, target), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertListEqual(sol.twoSum(nums, target), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertListEqual(sol.twoSum(nums, target), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
