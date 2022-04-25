import heapq
import unittest
from typing import List
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        h = []

        def inorder(node, x, y):
            if not node:
                return

            inorder(node.left, x-1, y+1)
            heapq.heappush(h, (x, y, node.val))
            inorder(node.right, x+1, y+1)

        inorder(root, 0, 0)
        res = []
        last_x = None
        while h:
            x, _, val = heapq.heappop(h)
            if x == last_x:
                res[-1].append(val)
            else:
                last_x = x
                res.append([val])
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
