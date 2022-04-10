import heapq
import unittest
from typing import List
from pprint import pprint


class Solution1:
    # LTE
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        # preprocessing
        res = 1
        for i, n in enumerate(nums):
            if n == 0 and k > 0:
                nums[i] = 1
                k -= 1
            res = res * nums[i]

        while k > 0:
            idx = 0
            m = 0

            for i, n in enumerate(nums):
                no_i_prod = res // n
                if no_i_prod > m:
                    m = no_i_prod
                    idx = i

            nums[idx] += 1
            res = m * nums[idx]
            k -= 1

        return res % MOD


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heappushpop(nums, nums[0]+1)
        res = 1
        for n in nums:
            res = (res * n) % MOD
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [0, 4]
        k = 5
        expected = 20
        self.assertEqual(sol.maximumProduct(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [6, 3, 3, 2]
        k = 2
        expected = 216
        self.assertEqual(sol.maximumProduct(nums, k), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [0]
        k = 5
        expected = 5
        self.assertEqual(sol.maximumProduct(nums, k), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [24, 5, 64, 53, 26, 38]
        k = 54
        expected = 180820950
        self.assertEqual(sol.maximumProduct(nums, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
