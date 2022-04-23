import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if p.val <= node.val <= q.val:
                return node

            if node.val < p.val:
                return helper(node.right)
            else:
                return helper(node.left)

        if p.val > q.val:
            p, q = q, p

        return helper(root)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        if p.val > q.val:
            p, q = q, p
        while not p.val <= node.val <= q.val:
            if node.val < p.val:
                node = node.right
            else:
                node = node.left
        return node


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
