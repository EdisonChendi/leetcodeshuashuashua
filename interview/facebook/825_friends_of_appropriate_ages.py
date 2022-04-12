import unittest
from typing import List
from pprint import pprint


class Solution1:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        ages.sort()
        i = j = 0
        N = len(ages)
        while i < N:
            cnt = 1
            while i < N-1 and ages[i] > 14 and ages[i] == ages[i+1]:
                i += 1
                cnt += 1
            while j < i and ages[j] <= 0.5*ages[i]+7:
                j += 1
                continue
            res += (i-j)*cnt
            i += 1
        return res


class Solution2:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        N = len(ages)
        ages.sort()
        left = right = 0
        for n in ages:
            if n <= 14:
                continue
            while ages[left] <= 0.5*n+7:
                left += 1
            while right+1 < N and ages[right+1] <= n:
                right += 1
            res += right - left
        return res


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        all_ages = [0]*121
        for n in ages:
            all_ages[n] += 1
        pre_sums = [0]
        for n in all_ages:
            pre_sums.append(pre_sums[-1]+n)

        res = 0
        for age in ages:
            if age < 15:
                continue
            left = 0.5 * age + 7
            res += pre_sums[age+1] - pre_sums[int(left)+1] - 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        ages = [20, 30, 100, 110, 120]
        expected = 3
        self.assertEqual(sol.numFriendRequests(ages), expected)

    def test_case_2(self):
        sol = Solution()
        ages = [16, 17, 18]
        expected = 2
        self.assertEqual(sol.numFriendRequests(ages), expected)

    def test_case_3(self):
        sol = Solution()
        ages = [16, 16]
        expected = 2
        self.assertEqual(sol.numFriendRequests(ages), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
