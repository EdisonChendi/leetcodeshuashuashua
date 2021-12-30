import heapq
import unittest
from typing import List
from pprint import pprint
import collections


class Solution1:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize != 0:
            return False

        hand.sort()
        candidates = collections.deque()
        for h in hand:
            for arr in candidates:
                if arr[0]+1 < h:
                    return False
                if arr[0] + 1 == h:
                    arr[0] = h
                    arr[1] += 1
                    if arr[1] == groupSize:
                        candidates.popleft()
                    break
            else:
                if groupSize > 1:
                    candidates.append([h, 1])

        return len(candidates) == 0


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize != 0:
            return False

        heapq.heapify(hand)
        cnt = collections.Counter(hand)
        while hand:
            h = heapq.heappop(hand)
            if cnt[h] == 0:
                continue
            for i in range(groupSize):
                if cnt[h+i] == 0:
                    return False
                cnt[h+i] -= 1
        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
        groupSize = 3
        expected = True
        self.assertEqual(sol.isNStraightHand(hand, groupSize), expected)

    def test_case_2(self):
        sol = Solution()
        hand = [1, 2, 3, 4, 5]
        groupSize = 4
        expected = False
        self.assertEqual(sol.isNStraightHand(hand, groupSize), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
