import random
import unittest
from typing import List
from pprint import pprint


class Solution:

    def quickselect(self, nums: List[int], k: int) -> int:
        return self._quickselect(nums, 0, len(nums)-1, k)

    def _partition(self, nums: List[int], left: int, right: int) -> int:
        rand_idx = random.randint(left, right)
        chosen = nums[rand_idx]
        nums[rand_idx], nums[right] = nums[right], nums[rand_idx]
        i = left
        for j in range(left, right):
            if nums[j] < chosen:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def _quickselect(self, nums: List[int], left: int, right: int, k: int) -> int:
        idx = self._partition(nums, left, right)
        if idx == k:
            return nums[idx]

        if idx > k:
            return self._quickselect(nums, left, idx-1, k)
        else:
            return self._quickselect(nums, idx+1, right, k)


def random_list(lo, hi, n):
    assert lo <= hi
    return [random.randint(lo, hi) for _ in range(n)]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        for _ in range(10):
            nums = random_list(1, 100, 15)
            k = random.randint(0, len(nums)-1)
            expected = sorted(nums)[k]
            self.assertEqual(sol.quickselect(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
