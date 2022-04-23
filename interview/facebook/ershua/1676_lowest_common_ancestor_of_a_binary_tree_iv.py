import unittest
from typing import List
from pprint import pprint


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)

        def helper(node):
            if not node:
                return None

            if node in nodes:
                return node

            left = helper(node.left)
            right = helper(node.right)

            if left and right:
                return node
            return left or right

        return helper(root)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
