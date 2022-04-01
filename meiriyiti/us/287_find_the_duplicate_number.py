import unittest
from typing import List
from pprint import pprint

class Solution1:
    # coding skills
    # does NOT satifies the problem(not changing the original array)
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = abs(nums[i])
            if nums[n] < 0:
                return n
            nums[n] = -abs(nums[n])

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pass


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,3,4,2,2]
        expected = 2
        self.assertEqual(sol.findDuplicate(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3,1,3,4,2]
        expected = 3
        self.assertEqual(sol.findDuplicate(nums), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
