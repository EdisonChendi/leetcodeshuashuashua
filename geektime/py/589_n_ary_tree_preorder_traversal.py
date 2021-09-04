import unittest
from typing import List
from pprint import pprint


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        def pre(node, accu):
            if not node:
                return accu
            accu.append(node.val)
            for n in node.children:
                pre(n, accu)
            return accu

        return pre(root, [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
