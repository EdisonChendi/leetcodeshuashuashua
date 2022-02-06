from itertools import count
import unittest
from typing import Counter, List
from pprint import pprint
import collections


class Solution1:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(n for n, cnt in collections.Counter(nums).items() if cnt == 1)


class Solution2:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        res = 0
        for n in nums:
            if n not in counter:
                res += n
            elif counter[n] == 1:
                res -= n
            counter[n] += 1
        return res


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        i, N = 0, len(nums)
        while i < N:
            ni = nums[i]
            j = i+1
            while j < N and nums[j] == ni:
                j += 1
            if j - i == 1:
                res += ni
            i = j
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3, 2]
        expected = 4
        self.assertEqual(sol.sumOfUnique(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 1, 1, 1, 1]
        expected = 0
        self.assertEqual(sol.sumOfUnique(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5]
        expected = 15
        self.assertEqual(sol.sumOfUnique(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
