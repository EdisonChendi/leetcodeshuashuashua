from ast import YieldFrom
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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        i = 0
        v = None

        def inorder(node: TreeNode):
            nonlocal i, v
            if not node:
                return

            inorder(node.left)
            i += 1
            if i == k:
                v = node.val
                raise
            inorder(node.right)

        try:
            inorder(root)
        except:
            pass
        finally:
            return v


class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = None
        it = inorder(root)
        for _ in range(k):
            ans = next(it)
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
