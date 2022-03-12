import unittest
from typing import List
from pprint import pprint

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def postorder(node, accu):
            if not node:
                return accu

            for child in node.children:
                postorder(child, accu)

            accu.append(node.val)
            return accu

        return postorder(root, [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
