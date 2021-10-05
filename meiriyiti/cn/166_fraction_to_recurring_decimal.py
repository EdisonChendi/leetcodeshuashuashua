import unittest
from typing import List
from pprint import pprint


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res, cache = [], {}
        i = 0
        sign = "-" if numerator * denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)

        int_part, remainder = divmod(numerator, denominator)
        while remainder > 0:
            numerator = remainder*10
            if numerator in cache:
                s, e = cache[numerator], i
                not_repeating = str(int_part) + "." + "".join(res[:s])
                repeating = "(" + "".join(res[s:e]) + ")"
                return sign+not_repeating+repeating

            quotient, remainder = divmod(numerator, denominator)
            res.append(str(quotient))
            cache[numerator] = i
            i += 1
        else:
            return sign+str(int_part) + (("." + "".join(res)) if res else "")


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        numerator = 1
        denominator = 2
        expected = "0.5"
        self.assertEqual(sol.fractionToDecimal(
            numerator, denominator), expected)

    def test_case_2(self):
        sol = Solution()
        numerator = 2
        denominator = 1
        expected = "2"
        self.assertEqual(sol.fractionToDecimal(
            numerator, denominator), expected)

    def test_case_3(self):
        sol = Solution()
        numerator = 2
        denominator = 3
        expected = "0.(6)"
        self.assertEqual(sol.fractionToDecimal(
            numerator, denominator), expected)

    def test_case_4(self):
        sol = Solution()
        numerator = 4
        denominator = 333
        expected = "0.(012)"
        self.assertEqual(sol.fractionToDecimal(
            numerator, denominator), expected)

    def test_case_5(self):
        sol = Solution()
        numerator = 1
        denominator = 5
        expected = "0.2"
        self.assertEqual(sol.fractionToDecimal(
            numerator, denominator), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
