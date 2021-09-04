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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def sub(inorder, begin, end):
            if begin == end:
                return None

            root = preorder.pop()
            root_index = inorder_map[root]
            return TreeNode(root,
                            sub(inorder, begin, root_index),
                            sub(inorder, root_index+1, end))

        preorder.reverse()
        inorder_map = {n: i for i, n in enumerate(inorder)}

        return sub(inorder, 0, len(preorder))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
