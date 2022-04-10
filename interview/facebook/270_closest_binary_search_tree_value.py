import unittest
from typing import List
from pprint import pprint


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        node = root

        res = node
        min_ = abs(node.val-target)

        while node:

            if target == node.val:
                return node.val

            if abs(target-node.val) < min_:
                min_ = abs(target-node.val)
                res = node

            node = node.right if target > node.val else node.left

        return res.val


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
