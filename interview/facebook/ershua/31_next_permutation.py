import unittest
from typing import List
from pprint import pprint


class Solution1:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # N - number of elements in nums
        # Time: O(N)
        # Space: O(N)
        N = len(nums)
        arr = [nums[-1]]
        for i in reversed(range(N-1)):
            n = nums[i]
            if n >= arr[-1]:
                arr.append(n)
            else:
                j = len(arr)-1
                while j > 0 and arr[j-1] > n:
                    j -= 1
                nums[i], arr[j] = arr[j], nums[i]
                nums[i+1:] = arr[:]
                break
        else:
            nums[:] = arr[:]


class Solution2:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            nums[:] = nums[::-1]
            return

        i, j = i-1, i
        while j < len(nums)-1 and nums[j+1] > nums[i]:
            j += 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])
        
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i < 0:
            nums[:] = nums[::-1]
        else:
            ni = nums[i]
            j = i
            while j < len(nums)-1 and nums[j+1] > ni:
                j += 1
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = nums[i+1:][::-1]



class TestSolution(unittest.TestCase):
    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 1]
        expected = [3, 1, 2]
        sol.nextPermutation(nums)
        self.assertListEqual(nums, expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 2, 3]
        expected = [1, 3, 2]
        sol.nextPermutation(nums)
        self.assertListEqual(nums, expected)

    def test_case_3(self):
        sol = Solution()
        nums = [3, 2, 1]
        expected = [1, 2, 3]
        sol.nextPermutation(nums)
        self.assertListEqual(nums, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
