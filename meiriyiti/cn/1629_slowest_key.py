import unittest
from typing import List
from pprint import pprint


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        r, k = releaseTimes[0], keysPressed[0]
        for i in range(1, len(releaseTimes)):
            cur_r = releaseTimes[i] - releaseTimes[i-1]
            if (cur_r, keysPressed[i]) >= (r, k):
                r, k = cur_r, keysPressed[i]
        return k


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        releaseTimes = [9, 29, 49, 50]
        keysPressed = "cbcd"
        expected = "c"
        self.assertEqual(sol.slowestKey(releaseTimes, keysPressed), expected)

    def test_case_2(self):
        sol = Solution()
        releaseTimes = [12, 23, 36, 46, 62]
        keysPressed = "spuda"
        expected = "a"
        self.assertEqual(sol.slowestKey(releaseTimes, keysPressed), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
