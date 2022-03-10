import unittest
from typing import List
from pprint import pprint


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def pre(node, res):
            if node is None:
                return res
            res.append(node.val)
            for child in node.children:
                pre(child, res)
            return res

        return pre(root, [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
