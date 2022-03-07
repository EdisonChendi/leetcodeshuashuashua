import unittest
from typing import List
from pprint import pprint

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        #BFS
        def valid(s:str)->bool:
            cnt = 0
            for ch in s:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    if cnt == 0:
                        return False
                    cnt -= 1
            return cnt == 0

        ans = set()
        q = set([s])
        while True:
            for ss in q:
                if valid(ss):
                    ans.add(ss)
            if ans:
                return ans
            nxt_q = set()
            while q:
                ss = q.pop()
                for i in range(len(ss)):
                    nxt_q.add(ss[:i]+ss[i+1:])
            q = nxt_q
        return list(ans)

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "()())()"
        expected = ["(())()","()()()"]
        self.assertCountEqual(sol.removeInvalidParentheses(s), expected)
        
    def test_case_2(self):
        sol = Solution()
        s = "(a)())()"
        expected = ["(a())()","(a)()()"]
        self.assertCountEqual(sol.removeInvalidParentheses(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = ")("
        expected = [""]
        self.assertCountEqual(sol.removeInvalidParentheses(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
