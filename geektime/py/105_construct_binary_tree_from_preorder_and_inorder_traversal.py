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
        preorder.reverse()
        inorder_map = {n: i for i, n in enumerate(inorder)}

        def sub(start, end):
            if start > end:
                return

            v = preorder.pop()
            split_idx = inorder_map[v]
            return TreeNode(val=v,
                            left=sub(start, split_idx-1),
                            right=sub(split_idx+1, end))

        return sub(0, len(preorder)-1)

    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def sub(preorder, inorder):

            if not inorder:
                return None

            v = preorder.pop()
            idx = inorder.index(v)
            return TreeNode(val=v,
                            left=sub(preorder, inorder[:idx]),
                            right=sub(preorder, inorder[idx+1:]))

        return sub(preorder[::-1], inorder)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
