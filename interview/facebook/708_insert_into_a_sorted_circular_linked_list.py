from code import interact
import unittest
from typing import List
from pprint import pprint

# Definition for a Node.


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head == None:
            node = Node(insertVal)
            node.next = node
            return node

        prev = head
        while True:
            cur = prev.next

            if cur is head:
                prev.next = Node(insertVal, head)
                return head

            if prev.val == insertVal or cur.val == insertVal:
                prev.next = Node(insertVal, cur)
                return head

            if (prev.val < insertVal < cur.val) \
                    or \
            (prev.val > cur.val and not prev.val > insertVal > cur.val):
                prev.next = Node(insertVal, cur)
                return head

            prev = cur


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
