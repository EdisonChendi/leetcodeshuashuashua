import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(node, accu):
            if not node:
                return accu
            accu.append(node.val)
            preorder(node.left, accu)
            preorder(node.right, accu)
            return accu
        
        return preorder(root, [])

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
        expected = [1,2,3]
        self.assertListEqual(sol.preorderTraversal(root), expected)
        
    def test_edge_case_1(self):
        sol = Solution()
        root = TreeNode(1)
        expected = [1]
        self.assertListEqual(sol.preorderTraversal(root), expected)


if __name__ == "__main__":
    unittest.main()
