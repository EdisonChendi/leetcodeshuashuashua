import unittest
from typing import List
from pprint import pprint

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        ds = (-1,0,1)
        stones_set = set(stones)
        stones_dict = {pos:idx for idx, pos in enumerate(stones)}
        N = len(stones)
        dp = [{}, {1,}]+[set() for _ in range(N-2)]
        for i in range(1, N):
            for k in dp[i]:
                for d in ds:
                    to = stones[i]+k+d
                    if to > stones[i] and to in stones_set:
                        dp[stones_dict[to]].add(k+d)

        return len(dp[-1]) > 0

    # LTE
    def canCross1(self, stones: List[int]) -> bool:
        ds = (-1,0,1)
        N = len(stones)
        dp = [(1, {1,}), ]
        for i in range(2, N):
            pos = stones[i]
            cur = set()
            for prev, ks in dp:
                for k in ks:
                    for delta in ds:
                        if prev+k+delta == pos:
                            cur.add(k+delta)
            if cur:
                dp.append((pos, cur))
        return dp[-1][0] == stones[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        stones = [0,1,3,5,6,8,12,17]
        expected = True
        self.assertEqual(sol.canCross(stones), expected)

    def test_case_2(self):
        sol = Solution()
        stones = [0,1,2,3,4,8,9,11]
        expected = False
        self.assertEqual(sol.canCross(stones), expected)

    def test_case_3(self):
        sol = Solution()
        stones = [0,1,3,5,6,8,12,17,18,19,21]
        expected = True
        self.assertEqual(sol.canCross(stones), expected)
        
    def test_edge_case_1(self):
        sol = Solution()
        stones = [0,2]
        expected = False
        self.assertEqual(sol.canCross(stones), expected)


if __name__ == "__main__":
    unittest.main()
