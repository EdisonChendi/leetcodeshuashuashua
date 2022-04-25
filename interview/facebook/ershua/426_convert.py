from os import preadv
import unittest
from typing import List
from pprint import pprint

# Definition for a Node.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        sentinel = Node(None)
        pre = sentinel

        def helper(node):
            nonlocal pre

            if node.left:
                helper(node.left)

            pre.right = node
            node.left = pre
            pre = node

            if node.right:
                helper(node.right)

        helper(root)
        pre.right = sentinel.right
        sentinel.right.left = pre
        return sentinel.right


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
