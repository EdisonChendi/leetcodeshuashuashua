from collections import deque
import unittest
from typing import List
from pprint import pprint

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution1:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            nxt_q = deque()
            cur = []
            while q:
                node = q.popleft()
                cur.append(node.val)
                for child in node.children:
                    nxt_q.append(child)
            q = nxt_q
            res.append(cur)
        return res


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        res = []
        prev = [root]
        while prev:
            cur = []
            cur_res = []
            for node in prev:
                cur_res.append(node.val)
                cur.extend(node.children)
            res.append(cur_res)
            prev = cur
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
