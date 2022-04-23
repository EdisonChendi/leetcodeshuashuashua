import math
from tkinter.messagebox import NO
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
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        par = {}

        def find(parent, node, k):
            if not node:
                return None
            par[node] = parent
            if node.val == k:
                return node
            return find(node, node.left, k) or find(parent, node.right, k)

        def dfs(from_, node, depth):
            nonlocal res, min_

            if not (node.left or node.right):
                if depth < min_:
                    min_ = min(min_, depth)
                    res = node.val
                return

            children = [node.left, node.right, par[node]]
            for ch in children:
                if ch and ch is not from_:
                    dfs(node, ch, depth+1)

        node_k = find(None, root, k)
        min_ = math.inf
        res = None
        dfs(None, node_k, 0)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
