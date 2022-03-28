from tokenize import Number
import unittest
from typing import List
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder(node, seq):
            if not node:
                return

            inorder(node.left)
            seq.append(node.val)
            inorder(node.right)
            return seq

        def build(left, right):
            if left > right:
                return None

            mid = (left+right) >> 1
            return TreeNode(seq[mid], build(left, mid-1), build(mid+1, right))

        seq = inorder(root, [])
        return build(0, len(seq)-1)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
