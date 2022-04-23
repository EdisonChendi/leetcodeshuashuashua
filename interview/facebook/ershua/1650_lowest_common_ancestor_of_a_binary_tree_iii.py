import unittest
from typing import List
from pprint import pprint

# Definition for a Node.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution1:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # time: O(max(Hp, hq))
        # space: O(max(Hp, hq))

        visisted = set()
        node = p
        while node:
            visisted.add(node)
            node = node.parent

        node = q
        while node:
            if node in visisted:
                return node

            node = node.parent


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # time: O(max(Hp, Hq))
        # space: O(1)
        np = p
        nq = q
        while np != nq:
            np = np.parent if np.parent else q
            nq = nq.parent if nq.parent else p
        else:
            return np


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
