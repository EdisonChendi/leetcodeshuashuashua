import unittest
from typing import List
from pprint import pprint

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        res = 0
        cur_max = 0

        def dfs(i, accu):
            nonlocal res, cur_max

            if i == len(nums):
                if accu == cur_max:
                    res += 1
                elif accu > cur_max:
                    cur_max = accu
                    res = 1
                return

            dfs(i+1, accu)
            dfs(i+1, accu|nums[i])
        
        dfs(0, 0)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3,1]
        expected = 2
        self.assertEqual(sol.countMaxOrSubsets(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [2,2,2]
        expected = 7
        self.assertEqual(sol.countMaxOrSubsets(nums), expected)
        
    def test_case_3(self):
        sol = Solution()
        nums = [3,2,1,5]
        expected = 6
        self.assertEqual(sol.countMaxOrSubsets(nums), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
