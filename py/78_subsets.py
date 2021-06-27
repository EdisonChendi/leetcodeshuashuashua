import unittest
from typing import List
from pprint import pprint


class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start, cur, accu):
            accu.append(cur[:])
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i+1, cur, accu)
                cur.pop()
            return accu

        return backtrack(0, [], [])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, cur, accu):
            if index == len(nums):
                accu.append(cur[:])
                return accu

            dfs(index+1, cur, accu)  # not choose
            cur.append(nums[index])
            dfs(index+1, cur, accu)  # choose
            cur.pop()

            return accu

        return dfs(0, [], [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3]
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        print(sol.subsets(nums))
        self.assertCountEqual(sol.subsets(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [0]
        expected = [[], [0]]
        self.assertCountEqual(sol.subsets(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
