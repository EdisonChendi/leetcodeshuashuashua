import unittest
from typing import List
from pprint import pprint


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        N = len(nums)
        move = [0]*N
        for i, n in enumerate(nums):
            if n <= i:
                move[0] += 1
                move[(i-n+1) % N] -= 1
                move[(i+1) % N] += 1
            else:
                move[(i+1) % N] += 1
                move[(N-(n-i)+1) % N] -= 1

        score = 0
        max_score = 0
        res = 0
        for i, m in enumerate(move):
            score += m
            if score > max_score:
                max_score = score
                res = i
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 1, 4, 0]
        exepcted = 3
        self.assertEqual(sol.bestRotation(nums), exepcted)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 3, 0, 2, 4]
        exepcted = 0
        self.assertEqual(sol.bestRotation(nums), exepcted)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
