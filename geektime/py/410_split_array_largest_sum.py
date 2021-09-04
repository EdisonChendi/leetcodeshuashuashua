import unittest
from typing import List
from pprint import pprint

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(mid):
            accu = 0
            cnt = 0
            for n in nums:
                if n > mid:
                    return False
                if accu+n > mid:
                    cnt += 1
                    accu = n
                else:
                    accu += n
            if accu > 0:
                cnt += 1
            return cnt <= m


        l, h = min(nums), sum(nums)
        while l <= h:
            mid = (l+h)>>1
            if check(mid):
                h = mid - 1
            else:
                l = mid + 1
        return l


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [7,2,5,10,8]
        m = 2
        expected = 18
        self.assertEqual(sol.splitArray(nums, m), expected)
        
    def test_case_2(self):
        sol = Solution()
        nums = [1,2,3,4,5]
        m = 2
        expected = 9
        self.assertEqual(sol.splitArray(nums, m), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [1,4,4]
        m = 3
        expected = 4
        self.assertEqual(sol.splitArray(nums, m), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
