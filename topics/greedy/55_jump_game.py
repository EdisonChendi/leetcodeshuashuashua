import unittest
from typing import List
from pprint import pprint


class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        longest = 0
        for i, n in enumerate(nums):
            if i <= longest:
                longest = max(i+n, longest)
                if longest >= N-1:
                    return True
            else:
                return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        reach = N-1
        for i in reversed(range(N-1)):
            if i + nums[i] >= reach:
                reach = i
        return reach == 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 1, 1, 4]
        expected = True
        self.assertEqual(sol.canJump(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
