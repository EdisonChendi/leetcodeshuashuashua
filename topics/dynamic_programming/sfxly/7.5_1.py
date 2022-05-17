import unittest
from typing import List
from pprint import pprint

class Node:

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_invitations(self, root: Node) -> int:
        # 自底向上，每个节点都可以 - 选，不选
        
        def dfs(node):
            y, n, Y, N = 1, 0, True, True
            for child in [node.left, node.right]:
                if not child: continue
                cy, cn, cY, cN = dfs(child)
                y += cn
                Y = Y and cN
                n += max(cy, cn)
                N = N and (False if cy == cn else (cY if cy > cn else cN))
            return y, n, Y, N
        
        y,n,Y,N = dfs(root)
        return max([y,n]), False if y == n else (Y if y > n else N)
            

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        root = Node("Jason",
                        left=Node("Jack", left=Node("Joe"), right=Node("John")),
                        right=Node("Jill", left=Node("Jim")))
        expected = (4, True)
        self.assertEqual(sol.max_invitations(root), expected)

    def test_case_2(self):
        sol = Solution()
        root = Node("Jason", left=Node("Jack"))
        expected = (1, False)
        self.assertEqual(sol.max_invitations(root), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
