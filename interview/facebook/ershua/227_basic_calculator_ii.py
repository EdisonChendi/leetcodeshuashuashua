import unittest
from typing import List
from pprint import pprint


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        pre_op = "+"
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = 10*num + int(ch)

            if i == len(s)-1 or ch in "+-*/":
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop()*num)
                elif pre_op == "/":
                    stack.append(int(stack.pop()/num))
                pre_op = ch
                num = 0

        return sum(stack)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "3+2*2"
        expected = 7
        self.assertEqual(sol.calculate(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "3/2"
        expected = 1
        self.assertEqual(sol.calculate(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
