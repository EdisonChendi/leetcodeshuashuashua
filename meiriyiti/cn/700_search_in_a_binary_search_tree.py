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
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None

        if val == root.val:
            return root

        return self.searchBST(root.left if val < root.val else root.right, val)


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val == root.val:
                return root
            root = root.left if val < root.val else root.right
        else:
            return None


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
