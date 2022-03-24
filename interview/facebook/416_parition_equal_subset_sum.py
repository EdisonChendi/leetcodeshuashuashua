import unittest
from typing import List
from pprint import pprint
import copy
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        SUM = sum(nums)
        if SUM % 2 != 0:
            return False

        half = SUM //2
        dp = set()
        for n in nums:
            for v in copy.copy(dp):
                if n+v == half: return True
                dp.add(n+v)
            if n == half: return True
            dp.add(n)
        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,5,11,5]
        expected = True
        self.assertEqual(sol.canPartition(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1,2,3,5]
        expected = False
        self.assertEqual(sol.canPartition(nums), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
