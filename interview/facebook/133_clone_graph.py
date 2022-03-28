import unittest
from typing import List
from pprint import pprint


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution1:
    # DFS
    def cloneGraph(self, node: 'Node') -> 'Node':
        cache = {}

        def dfs(node):
            if node.val in cache:
                return cache[node.val]

            clone = Node(node.val)
            cache[node.val] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        if not node:
            return node

        return dfs(node)


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # BFS
        if not node:
            return node

        cache = {node.val: Node(node.val)}
        q = [node]
        while q:
            nxt_q = []
            while q:
                n = q.pop()
                clone_n = cache[n.val]
                for nei in n.neighbors:
                    if nei.val not in cache:
                        clone_nei = Node(nei.val)
                        cache[nei.val] = clone_nei
                        nxt_q.append(nei)
                    clone_n.neighbors.append(cache[nei.val])
            q = nxt_q
        return cache[node.val]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
