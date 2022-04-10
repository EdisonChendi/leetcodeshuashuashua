import bisect
import unittest
from typing import List
from pprint import pprint


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:

        def get_low(flowers, newFlowers):
            if not flowers:
                return 0

            l = flowers[0]
            r = target - 1

            while l < r:
                mid = (l+r+1) >> 1
                idx = bisect.bisect_left(flowers, mid)
                require = idx*mid-pre_sum[idx]
                if require > newFlowers:
                    r = mid - 1
                else:
                    l = mid
            return l

        flowers.sort()
        pre_sum = [0]
        for i, f in enumerate(flowers):
            pre_sum.append(pre_sum[-1]+f)

        f_cnt = 0
        while flowers and flowers[-1] >= target:
            flowers.pop()
            f_cnt += 1

        if not flowers:
            return f_cnt * full

        N = len(flowers)
        ans = get_low(flowers, newFlowers) * partial + f_cnt * full

        for i in reversed(range(N)):
            garden = flowers[i]
            if newFlowers >= target-garden:
                flowers.pop()
                f_cnt += 1
                newFlowers -= target-garden
                beauty = get_low(flowers, newFlowers) * partial + f_cnt * full
                ans = max(ans, beauty)
            else:
                beauty = get_low(flowers, newFlowers) * partial + f_cnt * full
                ans = max(ans, beauty)
                break

        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        flowers = [1, 3, 1, 1]
        newFlowers = 7
        target = 6
        full = 12
        partial = 1
        expected = 14
        self.assertEqual(sol.maximumBeauty(
            flowers, newFlowers, target, full, partial), expected)

    def test_case_2(self):
        sol = Solution()
        flowers = [2, 4, 5, 3, 4, 5, 3]
        newFlowers = 2
        target = 5
        full = 2
        partial = 6
        expected = 24
        self.assertEqual(sol.maximumBeauty(
            flowers, newFlowers, target, full, partial), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
