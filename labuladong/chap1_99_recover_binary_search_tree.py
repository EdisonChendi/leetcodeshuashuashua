import unittest
from typing import List, Optional
from pprint import pprint

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack, node1, node2, prev, cur = [], None, None, None, root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if prev and prev.val > node.val:
                node2 = node
                if not node1:
                    node1 = prev
                else:
                    break
            prev, cur = node, node.right

        node1.val, node2.val = node2.val, node1.val

    def recoverTree1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # recursive - clean code
        node1, node2, prev = None, None, None

        def inorder(node):
            nonlocal node1, node2, prev

            if node is None:
                return

            inorder(node.left)
            if prev and prev.val > node.val:
                if not node1:
                    node1, node2 = prev, node
                else:
                    node2 = node
                    raise

            prev = node
            inorder(node.right)

        try:
            inorder(root)
        except:
            pass
        finally:
            node1.val, node2.val = node2.val, node1.val


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
