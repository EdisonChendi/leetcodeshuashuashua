import unittest
from typing import List
from pprint import pprint


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        count = 0
        for n in nums:
            if count == 0:
                element = n
                count = 1
            else:
                count += 1 if n == element else -1
        return element


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3, 2, 3]
        expected = 3
        self.assertEqual(sol.majorityElement(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [2, 2, 1, 1, 1, 2, 2]
        expected = 2
        self.assertEqual(sol.majorityElement(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
