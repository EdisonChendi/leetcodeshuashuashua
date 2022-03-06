import unittest
from typing import List
from pprint import pprint


OP_PREC = {'+': 1, '-': 1, '*': 2, '/': 2}
OP_FUNC = {
    '+': lambda a, b: a+b,
    '-': lambda a, b: a-b,
    '*': lambda a, b: a*b,
    '/': lambda a, b: a//b
}


class Tokenizer:

    def __init__(self, s: str) -> None:
        self.s = s
        self.cur = 0

    def is_end(self) -> bool:
        return self.cur == len(self.s)

    def skip_white_space(self):
        while not self.is_end() and self.s[self.cur] == " ":
            self.cur += 1

    def peek_next_token(self):
        old_pos = self.cur
        token = self.next_token()
        self.cur = old_pos
        return token

    def next_token(self):
        self.skip_white_space()

        if self.s[self.cur] in OP_PREC:
            token = self.s[self.cur]
            self.cur += 1
            return token

        num = []
        while not self.is_end() and str.isdigit(self.s[self.cur]):
            num.append(self.s[self.cur])
            self.cur += 1
        return int(''.join(num))


class Solution:
    def calculate(self, s: str) -> int:

        def parse(prec):
            res = tok.next_token()
            if tok.is_end():
                return res

            op = tok.peek_next_token()
            op_prec = OP_PREC[op]
            while op_prec > prec:
                tok.next_token()
                right = parse(op_prec)
                res = OP_FUNC[op](res, right)
                if tok.is_end():
                    break
                op = tok.peek_next_token()
                op_prec = OP_PREC[op]
            return res

        tok = Tokenizer(s.strip())
        return parse(0)


class TestSolution(unittest.TestCase):

    def test_case_0(self):
        sol = Solution()
        s = "3+2*2+8"
        expected = 15
        self.assertEqual(sol.calculate(s), expected)

    def test_case_1(self):
        sol = Solution()
        s = "3 +2 *2/2+10-13/2"
        expected = 9
        self.assertEqual(sol.calculate(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "3+2*2"
        expected = 7
        self.assertEqual(sol.calculate(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "3/2"
        expected = 1
        self.assertEqual(sol.calculate(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "3+5/2"
        expected = 5
        self.assertEqual(sol.calculate(s), expected)

    def test_case_5(self):
        sol = Solution()
        s = "1*2-3/4+5*6-7*8+9/10"
        expected = -24
        self.assertEqual(sol.calculate(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
