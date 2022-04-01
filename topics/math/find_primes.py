import unittest
from typing import List
from pprint import pprint
import math


def prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


class Solution:
    def slow_find_primes(self, start: int, end: int) -> List[int]:
        return [n for n in range(start, end+1) if prime(n)]

    def find_primes(self, start: int, end: int) -> List[int]:
        res = []
        marked = [False] * (end+1)
        for n in range(max(start, 2), end+1):
            if marked[n]:
                continue
            res.append(n)
            for i in range(n, end//n+1):
                marked[i*n] = True
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        start = 1
        end = 1000
        expected = sol.slow_find_primes(start, end)
        res = sol.find_primes(start, end)
        self.assertListEqual(res, expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
