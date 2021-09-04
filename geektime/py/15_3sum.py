import unittest
from typing import List
from pprint import pprint


def twoSum(nums, si, target):
    i, j = si, len(nums)-1
    res = []
    while i < j:
        if i > si and nums[i] == nums[i-1]:
            i = i+1
            continue
        if j < len(nums)-1 and nums[j] == nums[j+1]:
            j = j-1
            continue
        ni, nj = nums[i], nums[j]
        s = ni + nj
        if s == target:
            res.append([ni, nj])
            i, j = i+1, j-1
        elif s < target:
            i = i+1
        else:
            j = j-1
    return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]+nums[i+2] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            else:
                n = nums[i]
                res.extend([n, ]+r for r in twoSum(nums, i+1, -n))
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        res = sol.threeSum(nums)
        self.assertCountEqual(res, expected)

    def test_case_2(self):
        sol = Solution()
        nums = []
        expected = []
        res = sol.threeSum(nums)
        self.assertCountEqual(res, expected)

    def test_case_3(self):
        sol = Solution()
        nums = [0]
        expected = []
        res = sol.threeSum(nums)
        self.assertCountEqual(res, expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
