import math
import unittest
from typing import List
from pprint import pprint

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_len(node):
    l = 0
    while node:
        l += 1
        node = node.next
    return l


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        l = list_len(head)

        res = []
        split_len = math.ceil(l/k)
        while head:
            res.append(head)
            for _ in range(split_len-1):
                head = head.next
            if len(res) == k:
                break
            head.next, head = None, head.next
            l -= split_len
            split_len = math.ceil(l/(k-len(res)))

        if len(res) < k:
            res.extend([None]*(k-len(res)))

        return res

    def splitListToParts1(self, head: ListNode, k: int) -> List[ListNode]:
        l = list_len(head)

        res = []
        split, split_len, sentinel = 0, math.ceil(l/k), ListNode(next=head)
        while head:
            split += 1
            if split == split_len:
                res.append(sentinel.next)

                sentinel = ListNode(next=head.next)
                head.next, head = None, head.next
                if k == len(res):
                    break
                l -= split_len
                split, split_len = 0, math.ceil(l/(k-len(res)))
            else:
                head = head.next
        if len(res) < k:
            res.extend([None]*(k-len(res)))
        return res


def print_linkedlist(ll):
    n = ll
    while n:
        print(str(n.val), end="->" if n.next else "")
        n = n.next
    print()


def make_linkedlist(arr):
    sentinel = ListNode()
    node = sentinel
    for n in arr:
        cur = ListNode(n)
        node.next, node = cur, cur
    return sentinel.next


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        head = make_linkedlist([1, 2, 3])
        print_linkedlist(head)
        k = 5
        expected = [[1], [2], [3], [], []]
        res = sol.splitListToParts(head, k)
        for l in res:
            print_linkedlist(l)

    def test_case_2(self):
        sol = Solution()
        head = make_linkedlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        k = 3
        expected = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
        res = sol.splitListToParts(head, k)
        for l in res:
            print_linkedlist(l)
        # self.assertCountEqual(expected, res)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
