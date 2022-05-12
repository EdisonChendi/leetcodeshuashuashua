import unittest
from typing import List
from pprint import pprint


class Solution:
    def numberToWords(self, num: int) -> str:
        i = 0
        UNIT = ["", "Thousand", "Million", "Billion"]
        res = []

        A = ["", "One", "Two", "Three", "Four",
             "Five", "Six", "Seven", "Eight", "Nine"]
        B = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
             "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        C = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
             "Sixty", "Seventy", "Eighty", "Ninety"]

        def eng(n):
            if 1 <= n <= 9:
                return A[n]

            res = []
            if n // 100 > 0:
                res.append(" ".join([A[n//100], "Hundred"]).strip())
            n = n % 100
            if 10 <= n <= 19:
                res.append(B[n-10])
            else:
                res.append(" ".join([C[n//10], A[n % 10]]).strip())

            return " ".join(res).strip()

        if num == 0:
            return "Zero"

        while num > 0:
            num, rem = divmod(num, 1000)
            if rem > 0:
                res.append(" ".join([eng(rem), UNIT[i]]))
            i += 1

        return " ".join(reversed(res)).strip()


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = 12345
        expected = "Twelve Thousand Three Hundred Forty Five"
        self.assertEqual(sol.numberToWords(num), expected)

    def test_case_2(self):
        sol = Solution()
        num = 123
        expected = "One Hundred Twenty Three"
        self.assertEqual(sol.numberToWords(num), expected)

    def test_case_3(self):
        sol = Solution()
        num = 1234567
        expected = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        self.assertEqual(sol.numberToWords(num), expected)

    def test_edge_case_1(self):
        sol = Solution()
        num = 1
        expected = "One"
        self.assertEqual(sol.numberToWords(num), expected)

    def test_edge_case_2(self):
        sol = Solution()
        num = 13
        expected = "Thirteen"
        self.assertEqual(sol.numberToWords(num), expected)

    def test_edge_case_3(self):
        sol = Solution()
        num = 0
        expected = "Zero"
        self.assertEqual(sol.numberToWords(num), expected)


if __name__ == "__main__":
    unittest.main()
