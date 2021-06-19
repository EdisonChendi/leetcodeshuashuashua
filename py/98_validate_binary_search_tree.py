import unittest
from typing import List
from pprint import pprint

import math

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
    def isValidBST(self, root: TreeNode) -> bool:
        # root > max of left tree
        # root < min of right tree
        def sub(node):
            if not node:
                return True, math.inf, -math.inf

            lvalid, lmin, lmax = sub(node.left)
            if not lvalid or node.val <= lmax:
                return False, None, None

            rvalid, rmin, rmax = sub(node.right)
            if not rvalid or node.val >= rmin:
                return False, None, None

            return True, min(lmin, node.val), max(rmax, node.val)

        return sub(root)[0]


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, lower, upper):
            if not node:
                return True

            if not lower < node.val < upper:
                return False

            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

        return helper(root, -math.inf, math.inf)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        tree = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
        expected = True
        self.assertEqual(sol.isValidBST(tree), expected)

    def test_case_2(self):
        sol = Solution()
        tree = TreeNode(5, left=TreeNode(1), right=TreeNode(
            4, left=TreeNode(3), right=TreeNode(6)))
        expected = False
        self.assertEqual(sol.isValidBST(tree), expected)

    def test_case_3(self):
        sol = Solution()
        tree = TreeNode(5, left=TreeNode(1), right=TreeNode(
            8, left=TreeNode(3), right=TreeNode(6)))
        expected = False
        self.assertEqual(sol.isValidBST(tree), expected)
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
