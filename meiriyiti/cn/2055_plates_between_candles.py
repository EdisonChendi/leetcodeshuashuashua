import unittest
from typing import List
from pprint import pprint
import bisect


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        accu = []
        candles = []
        cur = 0
        for i, ch in enumerate(s):
            if ch == "*":
                cur += 1
            else:
                candles.append(i)
                accu.append(cur)
        ans = []
        for l, r in queries:
            l_idx = bisect.bisect_left(candles, l)
            r_idx = bisect.bisect_right(candles, r)-1
            if l_idx >= r_idx:
                ans.append(0)
            else:
                ans.append(accu[r_idx]-accu[l_idx])
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "**|**|***|"
        queries = [[2, 5], [5, 9]]
        expected = [2, 3]
        self.assertListEqual(sol.platesBetweenCandles(s, queries), expected)

    def test_case_2(self):
        sol = Solution()
        s = "***|**|*****|**||**|*"
        queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
        expected = [9, 0, 0, 0, 0]
        self.assertListEqual(sol.platesBetweenCandles(s, queries), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
