from heapq import merge
import unittest
from typing import List
from pprint import pprint
from collections import deque

# 分组是核心思想


class Solution1:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        stack = []
        for p in properties:
            while stack and stack[-1][1] < p[1]:
                stack.pop()
                ans += 1
            stack.append(p)
        return ans


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_def = 0
        ans = 0
        for _, def_ in properties:
            ans += max_def > def_
            max_def = max(max_def, def_)
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        properties = [[5, 5], [6, 3], [3, 6]]
        expected = 0
        self.assertEqual(sol.numberOfWeakCharacters(properties), expected)

    def test_case_2(self):
        sol = Solution()
        properties = [[2, 2], [3, 3]]
        expected = 1
        self.assertEqual(sol.numberOfWeakCharacters(properties), expected)

    def test_case_3(self):
        sol = Solution()
        properties = [[1, 5], [10, 4], [4, 3]]
        expected = 1
        self.assertEqual(sol.numberOfWeakCharacters(properties), expected)

    def test_case_4(self):
        sol = Solution()
        properties = [[1, 5], [10, 4], [4, 3]]
        expected = 1
        self.assertEqual(sol.numberOfWeakCharacters(properties), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
