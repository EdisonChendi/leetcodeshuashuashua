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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            res.append(node)
            inorder(node.right)

        inorder(root)
        N = len(res)
        s1, s2 = None, None
        for i in range(N-1):
            n1, n2 = res[i], res[i+1]
            if not s1 and n1.val > n2.val:
                s1 = n1
            if s1 and (n1.val > n2.val and (i+1 == N-1 or n2.val < res[i+2].val)):
                s2 = n2
        s1.val, s2.val = s2.val, s1.val


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
