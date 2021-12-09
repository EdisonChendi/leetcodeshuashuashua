import unittest
from typing import List
from pprint import pprint

'''
[meiriyiti][hard][dp]689_maximum_sum_of_3_non_overlapping_subarrays
1.dp - use table
2.needs careful coding
3.easy to come up with the basic idea, but difficult to get it right
4.one difficult part for me: the problem needs to get all the index, not just one value
'''

def cal_ksums(nums, k):
    res = [sum(nums[:k]),]
    for i in range(1,len(nums)-k+1):
        res.append(res[-1]-nums[i-1]+nums[i-1+k])
    return res

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        table = [list(zip([0]*(N+1), range(N+1), range(N+1))),]
        ksums = cal_ksums(nums, k)
        for _ in range(3):
            prev = table[-1]
            len_dp = len(prev)-k
            dp = [None,]*len_dp
            dp[-1] = (ksums[len_dp-1]+prev[len_dp-1+k][0], len_dp-1, len_dp-1+k)
            for j in reversed(range(len(dp)-1)):
                fj = ksums[j]+prev[j+k][0]
                if fj >= dp[j+1][0]:
                    dp[j] = (fj, j, j+k)
                else:
                    dp[j] = dp[j+1]
            table.append(dp)
        
        v3 = table[-1][0]
        for i in range(1, len(table[-1])):
            cur = table[-1][i]
            if cur[0] >= v3[0] and cur[1] < v3[1]:
                v3 = cur
        v2 = table[-2][v3[2]]
        v1 = table[-3][v2[2]]
        return [v3[1], v2[1], v1[1]]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,2,1,2,6,7,5,1]; k = 2
        expected =  [0,3,5]
        self.assertListEqual(sol.maxSumOfThreeSubarrays(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1,2,1,2,1,2,1,2,1]; k = 2
        expected =  [0,2,4]
        self.assertListEqual(sol.maxSumOfThreeSubarrays(nums, k), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
