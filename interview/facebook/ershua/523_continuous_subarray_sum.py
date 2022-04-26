import unittest
from typing import List
from pprint import pprint


class Solution1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            temp = total
            while temp >= k:
                if temp in seen and (i-seen[temp]) >= 2:
                    return True
                temp -= k
            seen[total] = i
        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        seen = {0: -1}
        for i, n in enumerate(nums):
            rem = (total+n) % k
            if rem in seen and i-seen[rem] >= 2:
                return True
            if rem not in seen:
                seen[rem] = i
            total += n
        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [23, 2, 4, 6, 7]
        k = 6
        expected = True
        self.assertEqual(sol.checkSubarraySum(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [23, 2, 6, 4, 7]
        k = 13
        expected = False
        self.assertEqual(sol.checkSubarraySum(nums, k), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [23, 2, 6, 4, 7]
        k = 6
        expected = True
        self.assertEqual(sol.checkSubarraySum(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
