import unittest
from typing import List
from pprint import pprint

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = [0]*200
        res = 0
        for n in nums:
            res += cnt[n+k] + cnt[n-k]
            cnt[n] += 1
        return res

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,2,2,1]; k = 1
        expected = 4
        self.assertEqual(sol.countKDifference(nums, k), expected)
        
    def test_case_2(self):
        sol = Solution()
        nums = [1,3]; k = 3
        expected = 0
        self.assertEqual(sol.countKDifference(nums, k), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [3,2,1,5,4]; k = 2
        expected = 3
        self.assertEqual(sol.countKDifference(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
