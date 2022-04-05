import unittest
from typing import List
from pprint import pprint


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        res = []
        n, r = divmod(n, 10)
        res.append(r)
        while n > 0:
            n, r = divmod(n, 10)
            if r <= res[-1]:
                res.append(r)
            else:
                res = [9]*len(res)
                res.append(r-1)
        return sum(n*(10**i) for i, n in enumerate(res))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 10
        expected = 9
        self.assertEqual(sol.monotoneIncreasingDigits(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1234
        expected = 1234
        self.assertEqual(sol.monotoneIncreasingDigits(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 332
        expected = 299
        self.assertEqual(sol.monotoneIncreasingDigits(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
