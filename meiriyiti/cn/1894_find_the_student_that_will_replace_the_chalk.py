import unittest
from typing import List
from pprint import pprint
from unittest.case import expectedFailure
import bisect


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        pre_sum = chalk[:]
        for i in range(1, len(chalk)):
            pre_sum[i] += pre_sum[i-1]

        remainder = k % pre_sum[-1]
        return bisect.bisect_right(pre_sum, remainder)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        chalk = [5, 1, 5]
        k = 22
        expected = 0
        self.assertEqual(sol.chalkReplacer(chalk, k), expected)

    def test_case_2(self):
        sol = Solution()
        chalk = [3, 4, 1, 2]
        k = 25
        expected = 1
        self.assertEqual(sol.chalkReplacer(chalk, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
