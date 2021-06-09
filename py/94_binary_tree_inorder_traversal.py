import unittest
from typing import List
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def inorder(node, res):
            if not node:
                return res
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
            return res

        return inorder(root, [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
        expected = [1, 3, 2]
        self.assertListEqual(sol.inorderTraversal(root), expected)

    def test_case_2(self):
        sol = Solution()
        root = TreeNode(1, left=TreeNode(2))
        expected = [2, 1]
        self.assertListEqual(sol.inorderTraversal(root), expected)

    def test_case_3(self):
        sol = Solution()
        root = TreeNode(1, right=TreeNode(2))
        expected = [1, 2]
        self.assertListEqual(sol.inorderTraversal(root), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
