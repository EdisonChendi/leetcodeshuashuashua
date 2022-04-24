import unittest
from typing import List
from pprint import pprint


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # mono stack
        # N - length of the heights
        # O(N)
        res = []
        stack = []
        for n in reversed(heights):
            cnt = 0
            while stack and n > stack[-1]:
                stack.pop()
                cnt += 1
            res.append(cnt+int(bool(stack)))
            stack.append(n)
        return list(reversed(res))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        heights = [10, 6, 8, 5, 11, 9]
        expected = [3, 1, 2, 1, 1, 0]
        self.assertListEqual(sol.canSeePersonsCount(heights), expected)

    def test_case_2(self):
        sol = Solution()
        heights = [5, 1, 2, 3, 10]
        expected = [4, 1, 1, 1, 0]
        self.assertListEqual(sol.canSeePersonsCount(heights), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
