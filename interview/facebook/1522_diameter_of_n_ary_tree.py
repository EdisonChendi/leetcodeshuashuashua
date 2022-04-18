import unittest
from typing import List
from pprint import pprint

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: 'Node') -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            m1, m2 = 0, 0
            for ch in node.children:
                l = dfs(ch)
                if l >= m1 >= m2:
                    m1, m2 = l, m1
                elif m1 >= l >= m2:
                    m1, m2 = m1, l
            res = max(res, m1+m2)
            return 1+max(m1, m2)

        dfs(root)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        root = Node(
            1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])
        expected = 3
        self.assertEqual(sol.diameter(root), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
