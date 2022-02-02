from collections import deque
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def decodeString(self, s: str) -> str:
        # parse and recurse
        res = []
        i = 0
        while i < len(s) and s[i].isalpha():
            res.append(s[i])
            i += 1
        res = "".join(res)

        digit = 0
        while i < len(s) and s[i].isdigit():
            digit *= 10
            digit += int(s[i])
            i += 1

        if digit > 0:
            o = i
            stack = ["[", ]
            assert i == len(s) or s[i] == "["
            i += 1
            while i < len(s) and stack:
                if s[i] == "]":
                    stack.pop()
                if s[i] == "[":
                    stack.append("[")
                i += 1
            e = i

            return res + digit*self.decodeString(s[o+1:e])+self.decodeString(s[e:])
        else:
            return res


class Solution2:

    def decodeString(self, s: str) -> str:
        i = 0

        def helper():
            nonlocal i
            res = []
            while i < len(s) and s[i] != ']':
                if s[i].isalpha():
                    res.append(s[i])
                    i += 1
                else:
                    k = 0
                    while s[i].isdigit():
                        k = k*10 + int(s[i])
                        i += 1
                    i += 1
                    res.append(k*helper())
                    i += 1
            return "".join(res)

        return helper()


class Solution:

    def decodeString(self, s: str) -> str:
        # using stack
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                cur = deque()
                while stack[-1] != '[':
                    cur.appendleft(stack.pop())
                stack.pop()  # pop '['

                digit = deque()
                while stack and stack[-1].isdigit():
                    digit.appendleft(stack.pop())
                stack.append(int("".join(digit)) * "".join(cur))

        return "".join(stack)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "3[a]2[bc]"
        expected = "aaabcbc"
        self.assertEqual(sol.decodeString(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "3[a2[c]]"
        expected = "accaccacc"
        self.assertEqual(sol.decodeString(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "2[abc]3[cd]ef"
        expected = "abcabccdcdcdef"
        self.assertEqual(sol.decodeString(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "a"
        expected = "a"
        self.assertEqual(sol.decodeString(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
