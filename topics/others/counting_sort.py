import unittest
from typing import List
from pprint import pprint


class Solution:

    def counting_sort(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0, ]*N
        counter = []
        for n in nums:
            if len(counter)-1 < n:
                counter.extend([0]*(n-len(counter)+1))
            counter[n] += 1

        for i in range(1, len(counter)):
            counter[i] += counter[i-1]

        for n in reversed(nums):
            res[counter[n]-1] = n
            counter[n] -= 1

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [0, 4, 1, 7, 5, 5, 6, 4, 3, 3, 4, 2, 1, 9, 8, 4, 6]
        expected = sorted(nums)
        self.assertListEqual(sol.counting_sort(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [0, 4, 1, 7, 100]
        expected = sorted(nums)
        self.assertListEqual(sol.counting_sort(nums), expected)
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
