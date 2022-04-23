from tkinter.messagebox import RETRY
import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def helper(node, p, q):
            if not node:
                return None, None, None

            ln, lp, lq = helper(node.left, p, q)
            rn, rp, rq = helper(node.right, p, q)

            if node is p:
                if lq or rq:
                    return node, p, q
                else:
                    return None, p, None
            elif node is q:
                if lp or rp:
                    return node, p, q
                else:
                    return None, None, q
            elif (not (ln or rn)) and (lp or rp) and (lq or rq):
                return node, lp or rp, lq or rq
            else:
                return ln or rn, lp or rp, lq or rq

        return helper(root, p, q)[0]


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # simplify the code

        def helper(node, p, q):
            if not node:
                return None, None, None

            ln, lp, lq = helper(node.left, p, q)
            rn, rp, rq = helper(node.right, p, q)

            if ln or rn:
                return ln or rn, None, None

            cur_p = (node if node.val == p.val else None) or (lp or rp)
            cur_q = (node if node.val == q.val else None) or (lq or rq)
            if cur_p and cur_q:
                return node, None, None
            return None, cur_p, cur_q

        return helper(root, p, q)[0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
