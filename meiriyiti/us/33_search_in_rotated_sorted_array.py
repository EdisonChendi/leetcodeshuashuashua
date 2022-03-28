import unittest
from typing import List
from pprint import pprint

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            m = (l+r)>>1
            nm = nums[m]
            nl, nr = nums[l],nums[r]
            if nm == target:
                return m
            if nm >= nums[0]:
                # on the left side of pivot
                if nl <= target < nm:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # on the right side of pivot
                if nm < target <= nr:
                    l = m + 1
                else:
                    r = m - 1
        return -1

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 0
        expected = 4
        self.assertEqual(sol.search(nums, target), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 3
        expected = -1
        self.assertEqual(sol.search(nums, target), expected)
        
    def test_case_3(self):
        sol = Solution()
        nums = [1]
        target = 0
        expected = -1
        self.assertEqual(sol.search(nums, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
