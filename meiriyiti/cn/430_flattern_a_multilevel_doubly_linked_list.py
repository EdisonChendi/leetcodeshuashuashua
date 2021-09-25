import unittest
from typing import List
from pprint import pprint


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def helper(node):
            cur_node, node_next, tail = node, node.next, node

            if node.child:
                child_h, child_t = helper(node.child)
                node.next, child_t.next, child_h.prev, node.child = child_h, node_next, node, None
                node, tail = child_t, child_t

            if node_next:
                next_h, next_t = helper(node_next)
                node.next, tail, next_h.prev = next_h, next_t, node

            return cur_node, tail

        if not head:
            return None

        return helper(head)[0]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
