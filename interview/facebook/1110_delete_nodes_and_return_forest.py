import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        res = {root}
        to_delete = set(to_delete)
        
        def helper(node):
            
            left, right = node.left, node.right
            if node.val in to_delete:
                to_delete.remove(node.val)
                node.left = node.right = None
                if node in res: res.remove(node)
                if left: res.add(left)
                if right: res.add(right)
                    
            if left:
                if left.val in to_delete:    
                    node.left = None  
                helper(left)
            
            if right:
                if right.val in to_delete:
                    node.right = None
                helper(right)
        
        helper(root)
        return list(res)

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
