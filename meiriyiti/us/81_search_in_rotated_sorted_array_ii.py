import unittest
from typing import List
from pprint import pprint

class Solution1:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1
        while l <= r:
            nl, nr = nums[l],nums[r]
            m = (l+r)>>1
            nm = nums[m]
            if nm == target:
                return True
            if nm == nl == nr:
                l += 1
                r -= 1
            elif nm >= nl:
                if nl <= target < nm:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nm < target <= nr:
                    l = m + 1
                else:
                    r = m - 1
        return False

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1
        while l <= r and nums[l] == nums[r]:
            if nums[l] == target:
                return True
            l += 1

        while l <= r:
            nl, nr = nums[l],nums[r]
            m = (l+r)>>1
            nm = nums[m]
            if nm == target:
                return True
            if nm >= nl:
                if nl <= target < nm:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nm < target <= nr:
                    l = m + 1
                else:
                    r = m - 1
        return False

class TestSolution(unittest.TestCase):

    def test_case_0(self):
        sol = Solution()
        nums = [1,0,1,1,1]; target = 0
        expected = True
        self.assertEqual(sol.search(nums, target), expected)

    def test_case_1(self):
        sol = Solution()
        nums = [2,5,6,0,0,1,2]; target = 0
        expected = True
        self.assertEqual(sol.search(nums, target), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [2,5,6,0,0,1,2]; target = 3
        expected = False
        self.assertEqual(sol.search(nums, target), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [2,5,5,6,6,6,6,0,0,1,2]; target = 7
        expected = False
        self.assertEqual(sol.search(nums, target), expected)
        
    def test_case_4(self):
        sol = Solution()
        nums = [2,5,5,6,6,6,6,0,0,1,2]; target = 6
        expected = True
        self.assertEqual(sol.search(nums, target), expected)
        
    def test_case_5(self):
        sol = Solution()
        nums = [2,5,5,6,6,6,6,0,0,1,2]; target = 2
        expected = True
        self.assertEqual(sol.search(nums, target), expected)

    def test_case_6(self):
        sol = Solution()
        nums = [1,1,1,1,1]; target = 1
        expected = True
        self.assertEqual(sol.search(nums, target), expected)

    def test_case_7(self):
        sol = Solution()
        nums = [1,1,1,1,1]; target = 2
        expected = False
        self.assertEqual(sol.search(nums, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
