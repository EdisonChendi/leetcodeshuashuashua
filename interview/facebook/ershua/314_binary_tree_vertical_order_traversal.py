import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # BFS
        q = [(root,0)]
        min_ = max_ = 0
        d = collections.defaultdict(list)
        while q:
            nxt_q = []
            for node,x in q:
                d[x].append(node.val)
                if node.left:
                    nxt_q.append((node.left,x-1))
                if node.right:
                    nxt_q.append((node.right, x+1))
                min_ = min(min_, x)
                max_ = max(max_, x)
            q = nxt_q

        return [d[x] for x in range(min_, max_+1) if x in d]
        

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
