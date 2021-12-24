import unittest
from typing import List
from pprint import pprint
import math
import random


class Solution:

    def counting_sort(self, nums: List[int], digit: int, radix: int) -> List[int]:
        res = [0, ]*len(nums)
        counter = [0, ]*radix
        for n in nums:
            d = n//(radix**digit) % radix
            counter[d] += 1

        for i in range(1, radix):
            counter[i] += counter[i-1]

        for n in reversed(nums):
            d = n//(radix**digit) % radix
            res[counter[d]-1] = n
            counter[d] -= 1

        return res

    def radix_sort(self, nums: List[int], radix: int) -> List[int]:
        k = int(math.log(max(nums), radix))+1
        res = nums
        for i in range(k):
            res = self.counting_sort(res, i, radix)
        return res


def random_seq(mi, ma, n):
    return [random.randint(mi, ma) for _ in range(n)]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        for _ in range(100):
            sol = Solution()
            nums = random_seq(0, 1000, 20)
            expected = sorted(nums)
            self.assertListEqual(sol.radix_sort(nums, 10), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
