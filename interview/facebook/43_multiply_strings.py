import unittest
from typing import List
from pprint import pprint


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def split(num):
            res = []
            L = len(num)
            for i in range(L):
                res.append((ord(num[i])-ord('0'))*10**(L-1-i))
            return res

        n1 = split(num1)
        n2 = split(num2)

        res = 0
        for n in n1:
            for m in n2:
                res += n*m
        return str(res)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num1 = "2"
        num2 = "3"
        expected = "6"
        self.assertEqual(sol.multiply(num1, num2), expected)

    def test_case_2(self):
        sol = Solution()
        num1 = "123"
        num2 = "456"
        expected = "56088"
        self.assertEqual(sol.multiply(num1, num2), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
