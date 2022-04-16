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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        accu = 0

        def helper(node):
            nonlocal accu

            if not node:
                return

            helper(node.right)
            node.val += accu
            accu = node.val
            helper(node.left)

        helper(root, 0)
        return root


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node, accu):
            if not node:
                return accu

            node.val += helper(node.right, accu)
            return helper(node.left, node.val)

        helper(root, 0)
        return root


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
