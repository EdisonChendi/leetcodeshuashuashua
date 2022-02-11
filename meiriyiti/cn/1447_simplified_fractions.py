import unittest
from typing import List
from pprint import pprint


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for a in range(1, n):
            for b in range(a+1, n+1):
                if gcd(b, a) == 1:
                    res.append(f"{a}/{b}")
        return res


# class TestGcd(unittest.TestCase):

#     def test_case_1(self):
#         a = 10
#         b = 4
#         expected = 2
#         self.assertEqual(gcd(a, b), expected)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 4
        expected = ["1/2", "1/3", "1/4", "2/3", "3/4"]
        self.assertCountEqual(sol.simplifiedFractions(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 3
        expected = ["1/2", "1/3", "2/3"]
        self.assertCountEqual(sol.simplifiedFractions(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 2
        expected = ["1/2"]
        self.assertCountEqual(sol.simplifiedFractions(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
