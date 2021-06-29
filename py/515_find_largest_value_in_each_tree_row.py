import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = [root]
        res = []
        while q:
            nxt_q = []
            cur_max = -math.inf
            for n in q:
                if n.val > cur_max:
                    cur_max = n.val
                if n.left:
                    nxt_q.append(n.left)
                if n.right:
                    nxt_q.append(n.right)
            q = nxt_q
            res.append(cur_max)
        return res
        




class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
