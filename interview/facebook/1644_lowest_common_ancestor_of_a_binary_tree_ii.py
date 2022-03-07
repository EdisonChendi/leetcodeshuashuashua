import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if not node:
                return None, None, None
            lroot, lp, lq = helper(node.left)
            rroot, rp, rq = helper(node.right)
            if lroot or rroot:
                return lroot or rroot, None, None
            cur_p = lp or rp or (node if node.val == p.val else None)
            cur_q = lq or rq or (node if node.val == q.val else None)
            if cur_p and cur_q:
                return node, None, None
            return None, cur_p, cur_q

        return helper(root)[0]
        

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
