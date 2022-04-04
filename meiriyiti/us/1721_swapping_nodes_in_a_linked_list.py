from distutils.dep_util import newer_pairwise
import unittest
from typing import List
from pprint import pprint

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    # def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        beg = None
        end = None
        N = 0

        def dfs(cur, accu):
            nonlocal N, beg, end

            if cur is None:
                N = accu
                return

            dfs(cur.next, accu+1)

            if accu == k-1:
                beg = cur

            if accu == N-k:
                end = cur

        dfs(head, 0)
        beg.val, end.val = end.val, beg.val
        return head


class Solution2:
    # def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        begin = end = None
        node = head
        i = 0
        while node:
            i += 1
            if end:
                end = end.next
            if i == k:
                begin = node
                end = head
            node = node.next
        begin.val, end.val = end.val, begin.val
        return head


class Solution:
    # def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        begin = head
        for _ in range(1, k):
            begin = begin.next
        end, right = head, begin.next
        while right:
            end = end.next
            right = right.next
        begin.val, end.val = end.val, begin.val
        return head


def make_linked_list(arr):
    sentinel = ListNode()
    prev = sentinel
    for n in arr:
        new_node = ListNode(n)
        prev.next = new_node
        prev = new_node
    return sentinel.next


def to_arr(ll):
    arr = []
    node = ll
    while node:
        arr.append(node.val)
        node = node.next
    return arr


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [1, 2, 3, 4, 5]
        ll = make_linked_list(arr)
        k = 2
        after = sol.swapNodes(ll, k)
        expected = [1, 4, 3, 2, 5]
        self.assertListEqual(to_arr(after), expected)

    def test_case_2(self):
        sol = Solution()
        arr = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
        ll = make_linked_list(arr)
        k = 5
        after = sol.swapNodes(ll, k)
        expected = [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
        self.assertListEqual(to_arr(after), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
