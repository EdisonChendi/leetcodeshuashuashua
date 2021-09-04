import unittest
from typing import List
from pprint import pprint


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:

        def level(trees, accu):
            if not trees:
                return accu
            l, n = [], []
            for r in trees:
                l.append(r.val)
                n.extend(r.children)
            accu.append(l)
            return level(n, accu)

        if not root:
            return []

        return level([root, ], [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
