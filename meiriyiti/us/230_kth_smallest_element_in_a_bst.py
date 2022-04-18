import unittest
from typing import List
from pprint import pprint
from unittest.result import failfast


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        i = 0
        res = None

        def inorder(node):
            nonlocal i, res
            if not node:
                return

            inorder(node.left)
            i += 1
            if i == k:
                res = node.val
                raise
            inorder(node.right)

        try:
            inorder(root)
        except:
            pass
        finally:
            return res


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        res = None
        gen = inorder(root)
        for _ in range(k):
            res = next(gen)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
