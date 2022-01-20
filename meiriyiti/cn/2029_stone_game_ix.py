import unittest
from typing import List
from pprint import pprint


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt0 = cnt1 = cnt2 = 0
        for s in stones:
            if (m := s % 3) == 0:
                cnt0 += 1
            elif m == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        if cnt0 % 2 == 0:
            return cnt1 > 0 and cnt2 > 0

        return abs(cnt1 - cnt2) > 2


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        stones = [2, 1]
        expected = True
        self.assertEqual(sol.stoneGameIX(stones), expected)

    def test_case_2(self):
        sol = Solution()
        stones = [2]
        expected = False
        self.assertEqual(sol.stoneGameIX(stones), expected)

    def test_case_3(self):
        sol = Solution()
        stones = [5, 1, 2, 4, 3]
        expected = False
        self.assertEqual(sol.stoneGameIX(stones), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
