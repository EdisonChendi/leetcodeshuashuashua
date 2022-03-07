import unittest
from typing import List
from pprint import pprint


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if p.val <= node.val <= q.val:
                return node
            
            if node.val > q.val:
                return helper(node.left)
            else:
                return helper(node.right)
                

        if p.val > q.val: 
            p,q = q,p
 
        return helper(root)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
