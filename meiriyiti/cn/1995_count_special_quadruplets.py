import unittest
from typing import List
from pprint import pprint

class Solution1:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        if nums[i]+nums[j]+nums[k] == nums[l]:
                            res += 1
        return res

import collections

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        N = len(nums)
        cnt = collections.defaultdict(int)
        ans = 0
        for b in reversed(range(1, N-2)):
            c = b + 1
            for d in range(c+1, N):
                cnt[nums[d]-nums[c]] += 1
            for a in range(b):
                ans += cnt[nums[a]+nums[b]]
        return ans



class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,2,3,6]
        expected = 1
        self.assertEqual(sol.countQuadruplets(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3,3,6,4,5]
        expected = 0
        self.assertEqual(sol.countQuadruplets(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1,1,1,3,5]
        expected = 4
        self.assertEqual(sol.countQuadruplets(nums), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
