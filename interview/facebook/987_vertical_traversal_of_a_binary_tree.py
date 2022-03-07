import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import heapq
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, row, col):
            if not node:
                return
            heapq.heappush(h, (col, row, node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)

        h = [] 
        dfs(root, 0, 0)
        prev_col = None
        res = []
        while h:
            col, row, v = heapq.heappop(h)
            if col == prev_col:
                res[-1].append(v)
            else:
                res.append([v])
            prev_col = col 
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
