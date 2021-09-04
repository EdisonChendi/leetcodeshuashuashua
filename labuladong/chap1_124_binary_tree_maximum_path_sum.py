import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -math.inf

        def sub(node):
            nonlocal res
            if not node:
                return -math.inf

            l, r = sub(node.left), sub(node.right)
            start_with_node = node.val + max(0, l, r)
            pass_through_node = node.val + l + r
            res = max(res, start_with_node, pass_through_node)
            return start_with_node

        sub(root)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
        expected = 6
        self.assertEqual(sol.maxPathSum(root), expected)

    def test_case_2(self):
        sol = Solution()
        root = TreeNode(-10,
                        left=TreeNode(9),
                        right=TreeNode(20,
                                       left=TreeNode(15),
                                       right=TreeNode(7))
                        )
        expected = 42
        self.assertEqual(sol.maxPathSum(root), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
