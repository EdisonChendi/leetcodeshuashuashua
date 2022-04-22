import unittest
from typing import List
from pprint import pprint


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = list(s)
        o = []
        c = []
        for i, ch in enumerate(s):
            if ch == '(':
                o.append(i)
            elif ch == ')':
                if o:
                    o.pop()
                else:
                    c.append(i)
        for i in o+c:
            res[i] = ''
        return "".join(res)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
