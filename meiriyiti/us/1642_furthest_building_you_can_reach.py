import unittest
from typing import List
from pprint import pprint
import math

class Solution1:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # LTE - O(len(heights)*ladders)
        dp = [0]*(ladders+1)
        i = 0
        while i < len(heights)-1:
            h, n = heights[i], heights[i+1]
            if h < n:
                d = n-h
                nxt = [0]*(ladders+1)
                if dp[0] + d <= bricks:
                    nxt[0] = dp[0] + d
                else:
                    nxt[0] = math.inf
                for j in range(1, ladders+1):
                    if dp[j] + d <= bricks:
                        nxt[j] = min(dp[j-1], dp[j]+d) 
                    else:
                        nxt[j] = dp[j-1]
                if not any(l < math.inf for l in nxt):
                    break
                dp = nxt
            i += 1
        return i

import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        L = len(heights)
        res = 0
        h = []
        while res < L-1:
            hi, hn = heights[res], heights[res+1]
            diff = hn - hi
            if diff > 0:
                heapq.heappush(h, -diff)
                bricks -= diff
                if bricks < 0:
                    if ladders == 0:
                        return res
                    else:
                        ladders -= 1
                        bricks -= heapq.heappop(h)
            res += 1
        return res

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        heights = [4,2,7,6,9,14,12]
        bricks = 5
        ladders = 1
        expected = 4
        self.assertEqual(sol.furthestBuilding(heights, bricks, ladders), expected)

    def test_case_2(self):
        sol = Solution()
        heights = [4,12,2,7,3,18,20,3,19]
        bricks = 10
        ladders = 2
        expected = 7
        self.assertEqual(sol.furthestBuilding(heights, bricks, ladders), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
