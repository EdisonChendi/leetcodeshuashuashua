import unittest
from typing import List
from pprint import pprint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Solution:
    def swapPairs1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        sentinel = ListNode(next=head)
        prv, cur = sentinel, head
        while cur and cur.next:
            nxt = cur.next
            prv.next, cur.next, nxt.next = nxt, nxt.next, cur
            prv, cur = cur, cur.next
        return sentinel.next

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = head.next
        head.next, new_head.next = self.swapPairs(new_head.next), head
        return new_head


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        l = make_linked_list([1, 2, 3, 4])
        print_linked_list(l)
        res = sol.swapPairs(l)
        print_linked_list(res)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
