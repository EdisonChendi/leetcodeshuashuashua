import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# conslution:
# 1. thin and tall - BFS
# 2. flat and short - DFS
# more towards a complete binary tree -> more tendency to use BFS

class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # N -> number of nodes in the tree
        # time: O(N)
        # space: O(N), in the worst case, proportional to N
        # or O(D), D - diameter of the tree
        # BFS
        if not root:
            return []
        q = [root]
        res = []
        while q:
            nxt_q = []
            res.append(q[-1].val)
            for node in q:
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)
            q = nxt_q
        return res


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # time: O(N), has to visit very node
        # space: O(H), maximum depth of recursion
        # DFS
        max_depth = -1
        res = []

        def dfs(node, depth):
            nonlocal res, max_depth
            if not node:
                return

            if depth > max_depth:
                max_depth = depth
                res.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
