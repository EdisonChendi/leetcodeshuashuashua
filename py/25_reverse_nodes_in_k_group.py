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


def rev(n, k):
    prv, cur = n, n.next
    for _ in range(1, k):
        nnxt = cur.next
        cur.next = prv
        prv, cur = cur, nnxt
    return prv, n


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # traverse k nodes, enough?
        # if NO -> return head
        # if YES -> reverse and recurse on next node
        cur = head
        for i in range(k):
            if cur is None:
                return head
            cur = cur.next
        h, t = rev(head, k)
        t.next = self.reverseKGroup(cur, k)
        return h


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        ll = make_linked_list([1, 2, 3, 4, 5])
        print_linked_list(ll)
        k = 2
        res = sol.reverseKGroup(ll, k)
        print_linked_list(res)

    def test_case_2(self):
        sol = Solution()
        ll = make_linked_list([1, 2, 3, 4, 5])
        print_linked_list(ll)
        k = 5
        res = sol.reverseKGroup(ll, k)
        print_linked_list(res)

    def test_case_3(self):
        sol = Solution()
        ll = make_linked_list([1, 2, 3, 4, 5])
        print_linked_list(ll)
        k = 1
        res = sol.reverseKGroup(ll, k)
        print_linked_list(res)

    def test_case_4(self):
        sol = Solution()
        ll = make_linked_list([1])
        print_linked_list(ll)
        k = 1
        res = sol.reverseKGroup(ll, k)
        print_linked_list(res)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
