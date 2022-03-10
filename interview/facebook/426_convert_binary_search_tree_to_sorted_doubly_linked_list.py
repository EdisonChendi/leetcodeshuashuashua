import unittest
from typing import List
from pprint import pprint


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def in_order(node):
            if node.left:
                left_first, left_last = in_order(node.left)
                node.left, left_last.right = left_last, node
            else:
                left_first, left_last = node, node

            if node.right:
                right_first, right_last = in_order(node.right)
                node.right, right_first.left = right_first, node
            else:
                right_first, right_last = node, node

            return left_first, right_last

        if not root:
            return None

        first, last = in_order(root)
        first.left, last.right = last, first

        return first


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        first, last = None, None

        def dfs(node):
            nonlocal first, last
            if not node:
                return

            dfs(node.left)

            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node

            dfs(node.right)

        if not root:
            return None

        dfs(root)
        first.left, last.right = last, first
        return first


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
