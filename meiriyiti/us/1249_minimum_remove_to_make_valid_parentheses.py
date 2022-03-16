import unittest
from typing import List
from pprint import pprint

class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        ps = []
        remove = []
        for i,ch in enumerate(s):
            if ch == ')':
                if ps:
                    ps.pop()
                else:
                    remove.append(i)
            elif ch == '(':
                ps.append(i)
        remove.extend(ps)
        res = []
        j = 0
        print(remove)
        for i,ch in enumerate(s):
            if j < len(remove) and i == remove[j]:
                j += 1
            else:
                res.append(ch)
        return "".join(res)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ss = list(s)
        o = []
        c = []
        for i, ch in enumerate(ss):
            if ch == '(':
                o.append(i)
            elif ch == ')':
                if not o:
                    c.append(i)
                else:
                    o.pop()
        for i in o+c:
            ss[i] = ''
        return ''.join(ss)
            

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "lee(t(c)o)de)"
        expected = "lee(t(c)o)de"
        self.assertEqual(sol.minRemoveToMakeValid(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "a)b(c)d"
        expected = "ab(c)d"
        self.assertEqual(sol.minRemoveToMakeValid(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "))(("
        expected = ""
        self.assertEqual(sol.minRemoveToMakeValid(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
