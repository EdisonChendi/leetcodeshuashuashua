import unittest
from typing import List
from pprint import pprint

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        r = []
        node = head
        while node:
            r.append(node)
            node = node.next

        def helper(lst, l, r):
            if l > r:
                return None
            mid = (l+r) >> 1
            root = lst[mid]
            root.left = helper(lst, l, mid-1)
            root.right = helper(lst, mid+1, r)
            return root

        return helper(r, 0, len(r)-1)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
