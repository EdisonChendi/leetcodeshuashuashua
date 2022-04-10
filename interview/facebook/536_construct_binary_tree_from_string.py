import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def str2tree(self, s: str):
        # recursion
        i = 0

        def helper(parent):
            nonlocal i

            while i < len(s):
                if s[i] == '(':
                    i += 1
                    node = helper(parent)
                    if not parent.left:
                        parent.left = node
                    else:
                        parent.right = node

                elif s[i] == ')':
                    i += 1
                    return parent

                elif s[i] == '-' or s[i].isdigit():
                    num = [s[i], ]
                    i += 1
                    while i < len(s) and s[i].isdigit():
                        num.append(s[i])
                        i += 1
                    cur = TreeNode(int("".join(num)))
                    helper(cur)
                    return cur

        return helper(None)


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        N = len(s)
        stack = []
        i = 0
        while i < N:
            ch = s[i]

            if ch == '(':
                i += 1
            elif ch == '-' or ch.isdigit():
                i += 1
                nums = [ch]
                while i < N and s[i].isdigit():
                    nums.append(s[i])
                    i += 1
                stack.append(TreeNode(int("".join(nums))))
            elif ch == ')':
                top = stack.pop()
                parent = stack[-1]
                if not parent.left:
                    parent.left = top
                else:
                    parent.right = top
                i += 1

        if not stack:
            return None

        return stack[0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "4(2(3)(1))(6(5))"
        sol.str2tree(s)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
