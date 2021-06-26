import unittest
from typing import List
from pprint import pprint


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[], ]
        res = []
        for i, n in enumerate(nums):
            for r in self.permute(nums[:i]+nums[i+1:]):
                r.append(n)
                res.append(r)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                    [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertCountEqual(sol.permute(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        self.assertCountEqual(sol.permute(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1]
        expected = [[1, ], ]
        self.assertCountEqual(sol.permute(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
