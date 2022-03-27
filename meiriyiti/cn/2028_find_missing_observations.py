import unittest
from typing import List
from pprint import pprint


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        missing_sum = (m+n)*mean-sum(rolls)
        avg = missing_sum/n
        if avg > 6 or avg < 1:
            return []
        q, r = divmod(missing_sum, n)
        return [q+1]*r + [q]*(n-r)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        rolls = [3, 2, 4, 3]
        mean = 4
        n = 2
        expected = [6, 6]
        self.assertCountEqual(sol.missingRolls(rolls, mean, n), expected)

    def test_case_2(self):
        sol = Solution()
        rolls = [1, 5, 6]
        mean = 3
        n = 4
        expected = [2, 3, 2, 2]
        self.assertCountEqual(sol.missingRolls(rolls, mean, n), expected)

    def test_case_3(self):
        sol = Solution()
        rolls = [1, 2, 3, 4]
        mean = 6
        n = 4
        expected = []
        self.assertCountEqual(sol.missingRolls(rolls, mean, n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
