import unittest
from typing import List
from pprint import pprint


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        fast, slow = head.next, head
        while not (fast is None or slow is None):
            if fast is slow:
                return True

            if fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        else:
            return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n0 = ListNode(3)
        n1 = ListNode(2)
        n2 = ListNode(0)
        n3 = ListNode(0)
        n0.next = n1
        n1.next = n2
        n2.next = n3
        n3.next = n1
        self.assertTrue(sol.hasCycle(n0))

    def test_case_2(self):
        sol = Solution()
        n0 = ListNode(1)
        n1 = ListNode(2)
        n0.next = n1
        n1.next = n0
        self.assertTrue(sol.hasCycle(n0))

    def test_case_3(self):
        sol = Solution()
        n0 = ListNode(1)
        n1 = ListNode(2)
        n2 = ListNode(3)
        n0.next = n1
        n1.next = n2
        self.assertFalse(sol.hasCycle(n0))

    def test_edge_case_1(self):
        sol = Solution()
        n0 = ListNode(1)
        self.assertFalse(sol.hasCycle(n0))

    def test_edge_case_2(self):
        sol = Solution()
        self.assertFalse(sol.hasCycle(None))

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
