import unittest
from typing import List
from pprint import pprint


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        domi = {1, 2, 3, 4, 5, 6}
        cnt_tp = [0]*7
        cnt_bt = [0]*7
        for t, b in zip(tops, bottoms):
            domi &= {t, b}
            if not domi:
                return -1
            cnt_tp[t] += 1
            cnt_bt[b] += 1

        ans = N = len(tops)
        for n in domi:
            ans = min(ans, N-cnt_tp[n], N-cnt_bt[n])
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        tops = [2, 1, 2, 4, 2, 2]
        bottoms = [5, 2, 6, 2, 3, 2]
        expected = 2
        self.assertEqual(sol.minDominoRotations(tops, bottoms), expected)

    def test_case_2(self):
        sol = Solution()
        tops = [3, 5, 1, 2, 3]
        bottoms = [3, 6, 3, 3, 4]
        expected = -1
        self.assertEqual(sol.minDominoRotations(tops, bottoms), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
