import unittest
from typing import List
from pprint import pprint


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, n in enumerate(nums):
            if i > k:
                window.remove(nums[i-k-1])
            if n in window:
                return True
            window.add(n)

        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3, 1]
        k = 3
        expected = True
        self.assertEqual(sol.containsNearbyDuplicate(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 0, 1, 1]
        k = 1
        expected = True
        self.assertEqual(sol.containsNearbyDuplicate(nums, k), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        expected = False
        self.assertEqual(sol.containsNearbyDuplicate(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
