import unittest
from typing import List
from pprint import pprint

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        a,b = nums[0],-1
        idx = 0
        for i in range(1,len(nums)):
            n = nums[i]
            if n > a:
                a, b, idx = n, a, i
            elif n > b:
                b = n
        return idx if a >= 2*b else -1

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3,6,1,0]
        expected = 1
        self.assertEqual(sol.dominantIndex(nums), expected)
        
    def test_case_2(self):
        sol = Solution()
        nums = [1,2,3,4]
        expected = -1
        self.assertEqual(sol.dominantIndex(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1]
        expected = 0
        self.assertEqual(sol.dominantIndex(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
