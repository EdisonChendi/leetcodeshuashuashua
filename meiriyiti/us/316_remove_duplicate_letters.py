from os import remove
import re
import unittest
from typing import List
from pprint import pprint
import collections

class Solution1:
    # LTE
    def removeDuplicateLetters(self, s: str) -> str:
        removes = {ch:n-1 for ch,n in collections.Counter(s).items() if n>1}
        ss = list(s)
        ans = 'z'*len(ss)

        def dfs(i):
            nonlocal ans
            if not removes:
                ans = min(ans, "".join(ss))
                return
            
            if i == len(ss):
                return

            ch = ss[i]
            if ch in removes:
                ss[i] = ""
                removes[ch] -=1
                if removes[ch] == 0:
                    del removes[ch]
                dfs(i+1)

                ss[i] = ch
                removes[ch] = 1 + removes.get(ch, 0)
                dfs(i+1)
            else:
                dfs(i+1)
        
        dfs(0)
        return ans

class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        # mono stack
        counter = collections.Counter(s)
        stack = []
        in_stack = set()

        for ch in s:
            counter[ch] -= 1
            if ch in in_stack:
                continue
            while stack and counter[stack[-1]] > 0 and stack[-1] >= ch:
                in_stack.remove(stack[-1])
                stack.pop()
            stack.append(ch)
            in_stack.add(ch)

        return "".join(stack)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # mono stack
        counter = collections.Counter(s)
        stack = []
        in_stack = [False]*26
        ord_a = ord('a')

        for ch in s:
            counter[ch] -= 1

            ord_ch = ord(ch)-ord_a
            if in_stack[ord_ch]: continue
            
            while stack and counter[stack[-1]] > 0 and stack[-1] >= ch:
                in_stack[ord(stack[-1])-ord_a] = False
                stack.pop()

            stack.append(ch)
            in_stack[ord_ch] = True

        return "".join(stack)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "bcabc"
        expected = "abc"
        self.assertEqual(sol.removeDuplicateLetters(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "cbacdcbc"
        expected = "acdb"
        self.assertEqual(sol.removeDuplicateLetters(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "leetcode"
        expected = "letcod"
        self.assertEqual(sol.removeDuplicateLetters(s), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
