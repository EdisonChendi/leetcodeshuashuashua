import unittest
from typing import List
from pprint import pprint
import bisect


class Solution1:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        N = len(ages)
        res = 0
        prev_v, prev_cnt = None, None
        for i in reversed(range(N)):
            x = ages[i]
            if x == prev_v:
                res += prev_cnt
            else:
                cnt = 0
                cond1 = 0.5*x+7
                if cond1 <= x:
                    idx = bisect.bisect_right(ages, cond1, 0, i)
                    cnt = i-idx
                prev_v = x
                prev_cnt = cnt
                res += cnt
        return res

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        pre_sums = [0]*121
        for age in ages:
            pre_sums[age] += 1
        for i in range(1, 121):
            pre_sums[i] += pre_sums[i-1]
        res = 0
        for age in ages:
            lower_bound = int(0.5*age)+8
            if lower_bound <= age:
                res += pre_sums[age] - pre_sums[lower_bound-1] - 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        ages = [16, 16]
        expected = 2
        self.assertEqual(sol.numFriendRequests(ages), expected)

    def test_case_2(self):
        sol = Solution()
        ages = [16, 17, 18]
        expected = 2
        self.assertEqual(sol.numFriendRequests(ages), expected)

    def test_case_3(self):
        sol = Solution()
        ages = [20, 30, 100, 110, 120]
        expected = 3
        self.assertEqual(sol.numFriendRequests(ages), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
