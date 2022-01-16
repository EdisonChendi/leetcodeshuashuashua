from random import random
import unittest
from typing import List, Optional
from pprint import pprint


import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.arr = []
        node = head
        while node:
            self.arr.append(node.val)
            node = node.next
        self.l = len(self.arr)

    def getRandom(self) -> int:
        return self.arr[random.randrange(self.l)]


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        i = 1
        ans = 0
        while node:
            if random.randrange(i) == 0:
                ans = node.val
            i += 1
            node = node.next
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        obj = Solution(head)
        print(obj.getRandom())
        print(obj.getRandom())
        print(obj.getRandom())
        print(obj.getRandom())
        print(obj.getRandom())
        print(obj.getRandom())
        print(obj.getRandom())
        print(obj.getRandom())
        print(obj.getRandom())
        print(obj.getRandom())
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
