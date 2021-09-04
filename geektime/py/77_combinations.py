import unittest
from typing import List
from pprint import pprint


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def sub(start, left, cur, accu):
            if left == 0:
                accu.append(cur)
                return accu

            for i in range(start, n-left+2):
                sub(i+1, left-1, cur+[i], accu)

            return accu

        return sub(1, k, [], [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 4
        k = 2
        expected = [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]
        self.assertCountEqual(sol.combine(n, k), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        k = 1
        expected = [[1, ], ]
        self.assertCountEqual(sol.combine(n, k), expected)

# def test_edge_case_1(self):
#     s = Solution()


if __name__ == "__main__":
    unittest.main()
