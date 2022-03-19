import random
import unittest
from typing import List
from pprint import pprint

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # reservior sampling
        cnt = 0
        pick = None
        node = self.head
        while node:
            cnt += 1
            if random.randrange(0, cnt) == 0:
                pick = node
            node = node.next
        return pick.val


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
