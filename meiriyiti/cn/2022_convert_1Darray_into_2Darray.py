import unittest
from typing import List
from pprint import pprint


class Solution1:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if len(original) != m*n:
            return res

        for i in range(m):
            res.append(original[i*n:(i+1)*n])

        return res


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []

        res = [[None, ]*n for _ in range(m)]

        for i in range(len(original)):
            res[i//n][i % n] = original[i]

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        original = [1, 2, 3, 4]
        m = 2
        n = 2
        expected = [[1, 2], [3, 4]]
        self.assertCountEqual(sol.construct2DArray(original, m, n), expected)

    def test_case_2(self):
        sol = Solution()
        original = [1, 2, 3, 4]
        m = 1
        n = 4
        expected = [[1, 2, 3, 4]]
        self.assertCountEqual(sol.construct2DArray(original, m, n), expected)

    def test_case_3(self):
        sol = Solution()
        original = [1, 2, 3, 4, 5, 6]
        m = 2
        n = 3
        expected = [[1, 2, 3], [4, 5, 6]]
        self.assertCountEqual(sol.construct2DArray(original, m, n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
