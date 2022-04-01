import math
import unittest
from typing import List
from pprint import pprint


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}

        def dfs(node):
            if not node:
                return False

            if node is target:
                return True

            if dfs(node.left):
                parents[node.left] = node
                return True
            elif dfs(node.right):
                parents[node.right] = node
                return True

            return False

        dfs(root)
        # run bfs on target
        q = [target]
        visited = {target}
        while q and k > 0:
            new_q = []
            while q:
                node = q.pop()
                for n in [node.left, node.right, parents.get(node, None)]:
                    if n and n not in visited:
                        visited.add(n)
                        new_q.append(n)
            q = new_q
            k -= 1

        if k == 0:
            return [n.val for n in q]
        else:
            return []


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
