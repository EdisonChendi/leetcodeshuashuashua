import unittest
from typing import List
from pprint import pprint
import collections
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        preds = ((lambda a, b: a < b, lambda a: a % 2 == 1),
                 (lambda a, b: a > b, lambda a: a % 2 == 0))
        # BFS
        level = 0
        q = collections.deque([root, ])
        while q:
            new_q = collections.deque()
            cmp, parity = preds[level % 2]
            while q:
                node = q.popleft()
                if not parity(node.val):
                    return False
                if q and not cmp(node.val, q[0].val):
                    return False
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
            level += 1
        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
