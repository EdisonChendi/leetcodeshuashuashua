import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        s = [str(root.val)]
        if root.right:
            s.extend([f"({self.tree2str(root.left)})",
                     f"({self.tree2str(root.right)})"])
        elif root.left:
            s.append(f"({self.tree2str(root.left)})")
        return "".join(s)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
