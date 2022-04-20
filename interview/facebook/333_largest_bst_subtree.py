import math
import imp
import unittest
from typing import List
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def helper(node):
            nonlocal res
            if not node:
                return 0, True, math.inf, -math.inf

            left, left_bst, left_min, left_max = helper(node.left)
            right, right_bst, right_min, right_max = helper(node.night)
            bst = all([left_bst, right_bst, left_max < node.val < right_min])
            if bst:
                res = max(res, 1+left+right)

            return 1+left+right, bst, min(left_min, node.val), max(right_max, node.righ)

        helper(root)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
