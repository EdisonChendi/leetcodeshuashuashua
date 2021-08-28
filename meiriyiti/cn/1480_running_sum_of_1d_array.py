import unittest
from typing import List
from pprint import pprint
import itertools
import operator


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(itertools.accumulate(nums, operator.add))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3, 4]
        expected = [1, 3, 6, 10]
        self.assertListEqual(sol.runningSum(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3, 1, 2, 10, 1]
        expected = [3, 4, 6, 16, 17]
        self.assertListEqual(sol.runningSum(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
