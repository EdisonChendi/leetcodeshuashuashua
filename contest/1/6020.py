import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(v % 2 == 0 for v in collections.Counter(nums).values())


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
