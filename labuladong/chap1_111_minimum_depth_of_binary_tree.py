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
    def minDepth(self, root: TreeNode) -> int:
        # use bfs
        if not root:
            return 0
        q = [root]
        depth = 1
        while q:
            new_q = []
            while q:
                node = q.pop()
                if not (node.left or node.right):
                    return depth
                else:
                    if node.left:
                        new_q.append(node.left)
                    if node.right:
                        new_q.append(node.right)
            depth += 1
            q = new_q


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
