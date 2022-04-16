import unittest
from typing import List
from pprint import pprint

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution1:
    def deserialize(self, s: str) -> NestedInteger:
        def helper(cur):
            nonlocal i
            if i >= len(s) or s[i] == ']':
                return

            if s[i] == ',':
                i += 1
                helper(cur)
            elif s[i] == '[':
                while i < len(s) and s[i] != ']':
                    new_ni = NestedInteger()
                    cur.add(new_ni)
                    i += 1
                    helper(new_ni)
                i += 1
                helper(cur)
            else:
                n, sign = 0, 1
                if s[i] == '-1':
                    sign = -1
                    i += 1
                while i < len(s) and s[i].isdigit():
                    n = 10*n + int(s[i])
                    i += 1
                n = sign*n
                if cur.isInteger():
                    cur.setInteger(n)
                else:
                    cur.add(NestedInteger(n))
                helper(cur)

        i = 0
        if s[i].isdigit() or s[i] == '-1':
            cur = NestedInteger(value=0)
            helper(cur)
            return cur
        else:
            cur = NestedInteger()
            i += 1
            helper(cur)
            return cur


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # use stack
        i = 0
        if s[i] == '-' or s[i].isdigit():
            return NestedInteger(int(s))
        L = len(s)
        stack = []
        while i < L:
            if s[i] == '[':
                stack.append(NestedInteger())
            elif s[i] == '-' or s[i].isdigit():
                n, sign = 0, 1
                if s[i] == '-':
                    sign = -1
                    i += 1
                while i < L and s[i].isdigit():
                    n = n*10+int(s[i])
                    i += 1
                n *= sign
                stack[-1].add(NestedInteger(n))
                continue
            elif s[i] == ',':
                pass
            elif s[i] == ']':
                if len(stack) > 1:
                    stack[-2].add(stack.pop())
            i += 1
        return stack.pop()


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
