import unittest
from typing import List
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node, seen):
            if not node:
                return False
            
            v = node.val
            if k-v in seen:
                return True
            seen.add(v)
            return dfs(node.left,seen) or dfs(node.right,seen)
        
        return dfs(root, set())

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def inorder(node, reverse=False):
            left, right = node.left, node.right
            if reverse:
                left, right = right, left
            if node.left: yield from inorder(node.left, reverse)
            yield node
            if node.right: yield from inorder(node.right, reverse)

        left_it = inorder(root, False);left = next(left_it)
        right_it = inorder(root, True);right = next(right_it)
        while left is not right:
            s = left.val+right.val
            if s == k: return True
            elif s < k: left = next(left_it)
            else: right = next(right_it)
        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
