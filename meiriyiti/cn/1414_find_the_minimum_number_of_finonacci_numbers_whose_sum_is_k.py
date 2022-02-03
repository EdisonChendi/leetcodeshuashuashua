import unittest
from typing import List
from pprint import pprint


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibo = [1, 1]
        while fibo[-1] < k:
            fibo.append(sum(fibo[-2:]))
        res, i = 0, len(fibo)-1
        while k > 0:
            if k >= fibo[i]:
                k -= fibo[i]
                res += 1
            i -= 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        k = 7
        expected = 2
        self.assertEqual(sol.findMinFibonacciNumbers(k), expected)

    def test_case_2(self):
        sol = Solution()
        k = 10
        expected = 2
        self.assertEqual(sol.findMinFibonacciNumbers(k), expected)

    def test_case_3(self):
        sol = Solution()
        k = 19
        expected = 3
        self.assertEqual(sol.findMinFibonacciNumbers(k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
