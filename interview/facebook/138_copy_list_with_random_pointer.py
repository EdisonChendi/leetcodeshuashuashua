import collections
import unittest
from typing import List
from pprint import pprint


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        indices = {}

        def helper(cur):
            if not cur:
                return None

            new = Node(cur.val)
            indices[cur] = new
            new.next = helper(cur.next)
            if cur.random:
                new.random = indices[cur.random]

            return new

        return helper(head)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
