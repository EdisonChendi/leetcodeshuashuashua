import unittest
from typing import List
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def sub(node, accu):
            if not node:
                return accu
            return max(sub(node.left, accu+1), sub(node.right, accu+1))

        return sub(root, 0)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
