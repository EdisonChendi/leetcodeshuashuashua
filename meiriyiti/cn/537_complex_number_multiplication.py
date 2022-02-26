import unittest
from typing import List
from pprint import pprint


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(num):
            r, i = num.split("+")
            return int(r), int(i[:-1])

        r1, i1 = parse(num1)
        r2, i2 = parse(num2)
        r = r1*r2-i1*i2
        i = r1*i2+r2*i1
        return f"{r}+{i}i"


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num1 = "1+1i"
        num2 = "1+1i"
        expected = "0+2i"
        self.assertEqual(sol.complexNumberMultiply(num1, num2), expected)

    def test_case_2(self):
        sol = Solution()
        num1 = "1+-1i"
        num2 = "1+-1i"
        expected = "0+-2i"
        self.assertEqual(sol.complexNumberMultiply(num1, num2), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
