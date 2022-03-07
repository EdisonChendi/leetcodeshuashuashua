import unittest
from typing import List
from pprint import pprint

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def find(root, node):
            if not root:
                return False
            if root.val == node.val:
                return True
            return find(root.left, node) or find(root.right, node)
       
        cur = p
        if find(p.left, q) or find(p.right, q):
            return cur
        prev, cur = cur, cur.parent
        while cur:
            if cur.val == q.val:
                return cur
            else:
                if (prev is cur.left and find(cur.right, q)) or (prev is cur.right and find(cur.left, q)):
                    return cur
                else:
                    cur = cur.parent


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
