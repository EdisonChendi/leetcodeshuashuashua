import unittest
from typing import List
from pprint import pprint

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, nxt = None, head
        while nxt:
            nxt.next, prev, nxt = prev, nxt, nxt.next
        return prev


def make_linked_list(l):
    sentinel = ListNode()
    prev = sentinel
    for v in l:
        n = ListNode(v)
        prev.next, prev = n, n
    return sentinel.next


def print_linked_list(l):
    while l:
        print(f"{l.val}"+("->" if l.next else ""), end="")
        l = l.next
    print()


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        head = make_linked_list([1, 2, 3, 4, 5])
        print_linked_list(head)
        res = sol.reverseList(head)
        print_linked_list(res)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
