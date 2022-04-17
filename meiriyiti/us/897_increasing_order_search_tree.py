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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node, l):
            if not node:
                return
            inorder(node.left, l)
            l.append(node)
            inorder(node.right, l)
            return l

        l = inorder(root, [])
        for n1, n2 in zip(l, l[1:]):
            n1.left = n2.left = None
            n1.right = n2
        return l[0]


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            inorder(node.right)

        res = self.cur = TreeNode(None)
        inorder(root)
        return res.right


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
