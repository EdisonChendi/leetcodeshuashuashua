import collections
import unittest
from typing import List
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # by prefix
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(node, cur):
            if not node:
                return 0
            cur += node.val
            res = prefix[cur-targetSum]
            prefix[cur] += 1
            res += dfs(node.left, cur)
            res += dfs(node.right, cur)
            prefix[cur] -= 1
            return res

        return dfs(root, 0)

    def pathSum1(self, root: TreeNode, targetSum: int) -> int:
        # method1
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return []

            accu = []
            for n in (v+node.val for v in [0, ]+dfs(node.left)+dfs(node.right)):
                res += n == targetSum
                accu.append(n)

            return accu

        dfs(root)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        root = TreeNode(10,
                        TreeNode(5,
                                 TreeNode(3,
                                          TreeNode(3),
                                          TreeNode(-2)),
                                 TreeNode(2,
                                          right=TreeNode(1))),
                        TreeNode(-3,
                                 right=TreeNode(11)))
        targetSum = 8
        expected = 3
        self.assertEqual(sol.pathSum(root, targetSum), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
